r"""Contain the implementation of a base class to easily wrap a tensor
generator into another tensor generator."""

from __future__ import annotations

__all__ = ["BaseWrapperTensorGenerator"]


from coola.utils.format import str_indent, str_mapping

from startorch.tensor.base import BaseTensorGenerator, setup_tensor_generator


class BaseWrapperTensorGenerator(BaseTensorGenerator):
    r"""Define a base class to easily wrap a tensor generator into
    another tensor generator.

    Note:
        It is possible to wrap a tensor generator into another tensor
        generator without using this base class. This class makes it
        more convenient and reduce duplicate code.

    Args:
        generator: The tensor generator or its configuration.
    """

    def __init__(self, generator: BaseTensorGenerator | dict) -> None:
        super().__init__()
        self._generator = setup_tensor_generator(generator)

    def __repr__(self) -> str:
        args = str_indent(str_mapping({"tensor": self._generator}))
        return f"{self.__class__.__qualname__}(\n  {args}\n)"
