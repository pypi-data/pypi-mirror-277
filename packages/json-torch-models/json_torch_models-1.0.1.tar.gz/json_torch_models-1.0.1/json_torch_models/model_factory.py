import json
from typing import Union, List

from json_torch_models.model import JsonPyTorchModel
from json_torch_models.utils import my_import, PackageLookupBin
from torch import nn


class ModelFactory:
    def __init__(self, json_path: str, lookup_packages: List[str] = None) -> None:
        """
        Given a path to a json model skeleton, helps builds a model, and verifies that the json is correct.
        :param json_path: The path to the json file to parse.
        :param lookup_packages: extra packages in which to look for modules.
        """
        if lookup_packages is not None:
            PackageLookupBin.lookup_paths.extend(lookup_packages)
        self.json_path = json_path
        self.model = None
        self.log_kwargs = None
        self._build_architecture()

    def _build_architecture(self) -> None:
        """
        Builds the model and stores it in self model variable.
        :return: Nothing
        """
        with open(self.json_path) as file:
            model_definition = json.load(file)

        if "LogKwargs" in model_definition.keys():
            self.log_kwargs = model_definition.pop('LogKwargs')
        else:
            self.log_kwargs = None
        if 'Only' in model_definition.keys():
            # This is to be used if you just want to point to a pre-writen network
            model = my_import(model_definition['Only']['ComponentClass'])
            self.model = model
            return
        if "Encoder" in model_definition.keys():
            ModelFactory._verify_unet_structure(model_definition)
            model_definition = ModelFactory._convert_unet_like_to_normal(model_definition)
        else:
            ModelFactory._verify_structure(model_definition)
        model = JsonPyTorchModel(model_definition['Tag'], model_definition['Children'])

        self.model = model

    def get_model(self) -> nn.Module:
        """
        Returns the generated model.
        """
        return self.model

    def get_log_kwargs(self) -> Union[dict, None]:
        """
        Returns the log args that were specified in the json.
        :return:
        """
        return self.log_kwargs

    @staticmethod
    def _convert_unet_like_to_normal(model_definition: dict) -> dict:
        """
        Convert a json that was defined with unet syntax into the normal fully sequential representation.
        :param model_definition: The model dictionary.
        :return: The updated model dictionary.
        """
        encoder_elements = model_definition['Encoder']
        middle_elements = model_definition['Middle']
        decoder_elements = model_definition['Decoder']

        sequential = []
        sequential += encoder_elements
        sequential += middle_elements
        sequential += decoder_elements

        new_root = {
            "Tag": "Parent",
            "Children": sequential
        }

        return new_root

    @staticmethod
    def _verify_structure(model_definition: dict) -> bool:
        """
        Verifies that the structure of a json model is valid.
        :param model_definition: The model dictionary to verify.
        :return: Returns true if valid, raises an exception otherwise.
        """
        keys = model_definition.keys()

        ModelFactory._validate_node(keys)

        if 'Tag' in keys:
            if not isinstance(model_definition['Tag'], str):
                raise InvalidJsonArchitectureException("'Tag' must be an instance of 'str'")

        if 'Children' in keys:
            if not isinstance(model_definition['Children'], list):
                raise InvalidJsonArchitectureException("'Children' must be an instance of 'list'")

        if 'ComponentClass' in keys:
            if not isinstance(model_definition['ComponentClass'], str):
                raise InvalidJsonArchitectureException("'ComponentClass' must be an instance of 'str'")

        if 'args' in keys:
            if not isinstance(model_definition['args'], dict):
                raise InvalidJsonArchitectureException("'args' must be an instance of 'dict'")

        if 'store_out' in keys:
            if not isinstance(model_definition['store_out'], str):
                raise InvalidJsonArchitectureException("'store_out' must be an instance of 'str'")

        if 'Tag' not in keys and 'ComponentClass' not in keys:
            raise InvalidJsonArchitectureException("You didn't define 'ComponentClass'")

        if 'Children' in keys:
            for child in list(model_definition['Children']):
                ModelFactory._verify_structure(child)

        return True

    @staticmethod
    def _verify_unet_structure(model_definition: dict) -> bool:
        """
        Verifies that the structure of a json model is valid.
        :param model_definition: The model dictionary to verify.
        :return: Returns true if valid, raises an exception otherwise.
        """
        keys = model_definition.keys()
        if not ('Encoder' in keys and 'Decoder' in keys and 'Middle' in keys) or len(keys) != 3:
            raise InvalidJsonArchitectureException("When defining a UNet like structure (you defined 'Encoder')" +
                                                   " you must define exactly: Encoder, Decoder, and Middle")
        if not (
                isinstance(model_definition['Encoder'], list) and
                isinstance(model_definition['Encoder'], list) and
                isinstance(model_definition['Encoder'], list)):
            raise InvalidJsonArchitectureException("When defining a UNet like structure (you defined 'Encoder')" +
                                                   " the portions should be defined as lists!")

        for element in model_definition['Encoder']:
            ModelFactory._verify_structure(element)
        for element in model_definition['Decoder']:
            ModelFactory._verify_structure(element)
        for element in model_definition['Middle']:
            ModelFactory._verify_structure(element)

        return True

    @staticmethod
    def _validate_node(keys) -> bool:
        """
        Verifies that the keys of a node are valid.
        :param keys: The list of keys.
        :return: Returns true if all keys are valid, raises an exception otherwise.
        """
        if 'Tag' in keys and 'Children' not in keys:
            raise InvalidJsonArchitectureException("You must define 'Tag' and 'Children' together.")
        if 'Tag' in keys and 'args' in keys:
            raise InvalidJsonArchitectureException("You cannot define 'Tag' and 'args' at the same level.")
        if 'ComponentClass' in keys and 'args' not in keys:
            raise InvalidJsonArchitectureException("You must define 'ComponentClass' and 'args' together.")
        return True


class InvalidJsonArchitectureException(Exception):
    """
    Exception raised when a user tries to build a model with invalid json.
    """

    def __init__(self, message="Invalid model architecture in json."):
        super().__init__(message)
