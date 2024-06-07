r"""Contain the implementation of tensor generators where the values are
sampled from a Cauchy distribution."""

from __future__ import annotations

__all__ = [
    "CauchyTensorGenerator",
    "RandCauchyTensorGenerator",
    "RandTruncCauchyTensorGenerator",
    "TruncCauchyTensorGenerator",
]

from typing import TYPE_CHECKING

from coola.utils.format import str_indent, str_mapping

from startorch.random import cauchy, rand_cauchy, rand_trunc_cauchy, trunc_cauchy
from startorch.tensor.base import BaseTensorGenerator, setup_tensor_generator

if TYPE_CHECKING:
    import torch


class CauchyTensorGenerator(BaseTensorGenerator):
    r"""Implement a class to generate tensor by sampling values from a
    Cauchy distribution.

    Args:
        loc: A tensor generator (or its configuration) to
            generate the location.
        scale: A tensor generator (or its configuration) to
            generate the scale.

    Example usage:

    ```pycon

    >>> from startorch.tensor import Cauchy, RandUniform
    >>> generator = Cauchy(
    ...     loc=RandUniform(low=-1.0, high=1.0), scale=RandUniform(low=1.0, high=2.0)
    ... )
    >>> generator
    CauchyTensorGenerator(
      (loc): RandUniformTensorGenerator(low=-1.0, high=1.0)
      (scale): RandUniformTensorGenerator(low=1.0, high=2.0)
    )
    >>> generator.generate((2, 6))
    tensor([[...]])

    ```
    """

    def __init__(self, loc: BaseTensorGenerator | dict, scale: BaseTensorGenerator | dict) -> None:
        super().__init__()
        self._loc = setup_tensor_generator(loc)
        self._scale = setup_tensor_generator(scale)

    def __repr__(self) -> str:
        args = str_indent(str_mapping({"loc": self._loc, "scale": self._scale}))
        return f"{self.__class__.__qualname__}(\n  {args}\n)"

    def generate(self, size: tuple[int, ...], rng: torch.Generator | None = None) -> torch.Tensor:
        return cauchy(
            loc=self._loc.generate(size=size, rng=rng),
            scale=self._scale.generate(size=size, rng=rng),
            generator=rng,
        )


class RandCauchyTensorGenerator(BaseTensorGenerator):
    r"""Implement a class to generate tensor by sampling values from a
    Cauchy distribution.

    Args:
        loc: The location/median of the Cauchy distribution.
        scale: The scale of the distribution.

    Raises:
        ValueError: if ``scale`` is not a positive number.

    Example usage:

    ```pycon

    >>> from startorch.tensor import RandCauchy
    >>> generator = RandCauchy(loc=0.0, scale=1.0)
    >>> generator
    RandCauchyTensorGenerator(loc=0.0, scale=1.0)
    >>> generator.generate((2, 6))
    tensor([[...]])

    ```
    """

    def __init__(self, loc: float = 0.0, scale: float = 1.0) -> None:
        super().__init__()
        self._loc = float(loc)
        if scale <= 0:
            msg = f"scale has to be greater than 0 (received: {scale})"
            raise ValueError(msg)
        self._scale = float(scale)

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}(loc={self._loc}, scale={self._scale})"

    def generate(self, size: tuple[int, ...], rng: torch.Generator | None = None) -> torch.Tensor:
        return rand_cauchy(
            size=size,
            loc=self._loc,
            scale=self._scale,
            generator=rng,
        )


class RandTruncCauchyTensorGenerator(BaseTensorGenerator):
    r"""Implement a class to generate tensor by sampling values from a
    truncated Cauchy distribution.

    Args:
        loc: The location/median of the Cauchy distribution.
        scale: The scale of the distribution.
        min_value: The minimum value (included).
        max_value: The maximum value (excluded).

    Raises:
        ValueError: if ``std`` is not a positive number.
        ValueError: if ``max_value`` is lower than ``min_value``.

    Example usage:

    ```pycon

    >>> from startorch.tensor import RandTruncCauchy
    >>> generator = RandTruncCauchy(loc=0.0, scale=1.0, min_value=-1.0, max_value=1.0)
    >>> generator
    RandTruncCauchyTensorGenerator(loc=0.0, scale=1.0, min_value=-1.0, max_value=1.0)
    >>> generator.generate((2, 6))
    tensor([[...]])

    ```
    """

    def __init__(
        self,
        loc: float = 0.0,
        scale: float = 1.0,
        min_value: float = -2.0,
        max_value: float = 2.0,
    ) -> None:
        super().__init__()
        self._loc = float(loc)
        if scale <= 0:
            msg = f"scale has to be greater than 0 (received: {scale})"
            raise ValueError(msg)
        self._scale = float(scale)
        if max_value < min_value:
            msg = f"max_value ({max_value}) has to be greater or equal to min_value ({min_value})"
            raise ValueError(msg)
        self._min_value = float(min_value)
        self._max_value = float(max_value)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__qualname__}(loc={self._loc}, scale={self._scale}, "
            f"min_value={self._min_value}, max_value={self._max_value})"
        )

    def generate(self, size: tuple[int, ...], rng: torch.Generator | None = None) -> torch.Tensor:
        return rand_trunc_cauchy(
            size=size,
            loc=self._loc,
            scale=self._scale,
            min_value=self._min_value,
            max_value=self._max_value,
            generator=rng,
        )


class TruncCauchyTensorGenerator(BaseTensorGenerator):
    r"""Implement a class to generate tensor by sampling values from a
    Cauchy distribution.

    Args:
        loc: A tensor generator (or its configuration) to
            generate the location.
        scale: A tensor generator (or its configuration) to
            generate the scale.
        min_value: A tensor generator (or its configuration)
            to generate the minimum value (included).
        max_value: A tensor generator (or its configuration)
            to generate the maximum value (excluded).

    Example usage:

    ```pycon

    >>> from startorch.tensor import RandUniform, TruncCauchy
    >>> generator = TruncCauchy(
    ...     loc=RandUniform(low=-1.0, high=1.0),
    ...     scale=RandUniform(low=1.0, high=2.0),
    ...     min_value=RandUniform(low=-10.0, high=-5.0),
    ...     max_value=RandUniform(low=5.0, high=10.0),
    ... )
    >>> generator
    TruncCauchyTensorGenerator(
      (loc): RandUniformTensorGenerator(low=-1.0, high=1.0)
      (scale): RandUniformTensorGenerator(low=1.0, high=2.0)
      (min_value): RandUniformTensorGenerator(low=-10.0, high=-5.0)
      (max_value): RandUniformTensorGenerator(low=5.0, high=10.0)
    )
    >>> generator.generate((2, 6))
    tensor([[...]])

    ```
    """

    def __init__(
        self,
        loc: BaseTensorGenerator | dict,
        scale: BaseTensorGenerator | dict,
        min_value: BaseTensorGenerator | dict,
        max_value: BaseTensorGenerator | dict,
    ) -> None:
        super().__init__()
        self._loc = setup_tensor_generator(loc)
        self._scale = setup_tensor_generator(scale)
        self._min_value = setup_tensor_generator(min_value)
        self._max_value = setup_tensor_generator(max_value)

    def __repr__(self) -> str:
        args = str_indent(
            str_mapping(
                {
                    "loc": self._loc,
                    "scale": self._scale,
                    "min_value": self._min_value,
                    "max_value": self._max_value,
                }
            )
        )
        return f"{self.__class__.__qualname__}(\n  {args}\n)"

    def generate(self, size: tuple[int, ...], rng: torch.Generator | None = None) -> torch.Tensor:
        return trunc_cauchy(
            loc=self._loc.generate(size=size, rng=rng),
            scale=self._scale.generate(size=size, rng=rng),
            min_value=self._min_value.generate(size=size, rng=rng),
            max_value=self._max_value.generate(size=size, rng=rng),
            generator=rng,
        )
