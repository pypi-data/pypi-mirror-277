import torch
import torch.nn as nn

from json_torch_models.utils import my_import


class JsonPyTorchModel(nn.Module):

    def __init__(self, tag: str, children: list) -> None:
        """
        Builds a module based on a list of children.
        :param tag: Name for the current module. Does nothing.
        :param children: List of children in dictionary form.
        """
        super(JsonPyTorchModel, self).__init__()
        self.tag = tag
        self.child_modules = children
        self.data = {}
        self.network_modules = nn.ModuleList([])
        self.sequences = {}
        self._construct()

    def _construct(self) -> None:
        """
        Constructs the internal module based on children list.
        :return: None
        """
        for child in self.child_modules:
            if 'Tag' in child.keys():
                self.network_modules.append(JsonPyTorchModel(
                    child['Tag'],
                    child['Children']
                ))

            elif 'store_out' not in child.keys() and 'forward_in' not in child.keys():
                module = my_import(child['ComponentClass'])
                self.network_modules.append(
                    module=module(**(child['args']))
                )
            else:
                # New operation
                this_operation = {}
                # Store module
                self.network_modules.append(
                    module=my_import(child['ComponentClass'])(**(child['args']))
                )
                if 'store_out' in child.keys():
                    this_operation['store_out'] = child['store_out']
                if 'forward_in' in child.keys():
                    if not isinstance(child['forward_in'], dict):
                        child['forward_in'] = {
                            child['forward_in']: child['forward_in']
                        }
                    this_operation['forward_in'] = child['forward_in']

                self.sequences[len(self.network_modules) - 1] = this_operation

    def forward(self, *x: torch.Tensor) -> torch.Tensor:
        """
        Performs the forward pass and manages skipped connections.
        :param x: The data to compute.
        :return: The output data.
        """
        for i, module in enumerate(self.network_modules):

            if i not in self.sequences.keys():
                x = module(*x)
            else:
                operation = self.sequences[i]
                if 'forward_in' in operation.keys():
                    # Replace the map of "key" : "variable" with "key" : value
                    forward_in = {}
                    for key, value in operation['forward_in'].items():
                        forward_in[key] = self.data[value]
                    x = module(*x, forward_in)

                else:
                    x = module(*x)

                if 'store_out' in operation.keys():
                    self.data[operation['store_out']] = x

        return x
