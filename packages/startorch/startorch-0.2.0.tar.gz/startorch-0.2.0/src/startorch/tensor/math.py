r"""Contain the implementation of tensor generators that computes
arithmetic functions on tensors."""

from __future__ import annotations

__all__ = [
    "AbsTensorGenerator",
    "AddScalarTensorGenerator",
    "AddTensorGenerator",
    "ClampTensorGenerator",
    "DivTensorGenerator",
    "ExpTensorGenerator",
    "FmodTensorGenerator",
    "LogTensorGenerator",
    "MulScalarTensorGenerator",
    "MulTensorGenerator",
    "NegTensorGenerator",
    "SqrtTensorGenerator",
    "SubTensorGenerator",
]

from typing import TYPE_CHECKING

from coola.utils.format import str_indent, str_mapping, str_sequence

from startorch.tensor.base import BaseTensorGenerator, setup_tensor_generator
from startorch.tensor.wrapper import BaseWrapperTensorGenerator

if TYPE_CHECKING:
    from collections.abc import Sequence

    import torch


class AbsTensorGenerator(BaseWrapperTensorGenerator):
    r"""Implement a tensor generator that computes the absolute value of
    a tensor.

    This tensor generator is equivalent to: ``output = abs(tensor)``

    Example usage:

    ```pycon

    >>> from startorch.tensor import Abs, RandNormal
    >>> generator = Abs(RandNormal())
    >>> generator
    AbsTensorGenerator(
      (tensor): RandNormalTensorGenerator(mean=0.0, std=1.0)
    )
    >>> generator.generate((2, 6))
    tensor([[...]])

    ```
    """

    def generate(self, size: tuple[int, ...], rng: torch.Generator | None = None) -> torch.Tensor:
        return self._generator.generate(size=size, rng=rng).abs()


class AddScalarTensorGenerator(BaseWrapperTensorGenerator):
    r"""Implement a tensor generator that adds a scalar value to a
    generated batch of tensors.

    This tensor generator is equivalent to:
    ``output = tensor + scalar``

    Args:
        generator: The tensor generator or its configuration.
        value: The scalar value to add.

    Example usage:

    ```pycon

    >>> from startorch.tensor import AddScalar, RandUniform
    >>> generator = AddScalar(RandUniform(), 10.0)
    >>> generator
    AddScalarTensorGenerator(
      (tensor): RandUniformTensorGenerator(low=0.0, high=1.0)
      (value): 10.0
    )
    >>> generator.generate((2, 6))
    tensor([[...]])

    ```
    """

    def __init__(
        self,
        generator: BaseTensorGenerator | dict,
        value: float,
    ) -> None:
        super().__init__(generator=generator)
        self._value = value

    def __repr__(self) -> str:
        args = str_indent(str_mapping({"tensor": self._generator, "value": self._value}))
        return f"{self.__class__.__qualname__}(\n  {args}\n)"

    def generate(self, size: tuple[int, ...], rng: torch.Generator | None = None) -> torch.Tensor:
        tensor = self._generator.generate(size=size, rng=rng)
        tensor.add_(self._value)
        return tensor


class AddTensorGenerator(BaseTensorGenerator):
    r"""Implement a tensor generator that adds several tensor.

    This tensor generator is equivalent to:
    ``output = tensor_1 + tensor_2 + ... + tensor_n``

    Args:
        generators: The tensor generators.

    Raises:
        ValueError: if no sequence generator is provided.

    Example usage:

    ```pycon

    >>> from startorch.tensor import Add, RandNormal, RandUniform
    >>> generator = Add([RandUniform(), RandNormal()])
    >>> generator
    AddTensorGenerator(
      (0): RandUniformTensorGenerator(low=0.0, high=1.0)
      (1): RandNormalTensorGenerator(mean=0.0, std=1.0)
    )
    >>> generator.generate((2, 6))
    tensor([[...]])

    ```
    """

    def __init__(self, generators: Sequence[BaseTensorGenerator | dict]) -> None:
        super().__init__()
        if not generators:
            msg = "No tensor generator. You need to specify at least one tensor generator"
            raise ValueError(msg)
        self._generators = tuple(setup_tensor_generator(tensor) for tensor in generators)

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}(\n  {str_indent(str_sequence(self._generators))}\n)"

    def generate(self, size: tuple[int, ...], rng: torch.Generator | None = None) -> torch.Tensor:
        output = self._generators[0].generate(size=size, rng=rng)
        for generator in self._generators[1:]:
            output.add_(generator.generate(size=size, rng=rng))
        return output


class ClampTensorGenerator(BaseWrapperTensorGenerator):
    r"""Implement a tensor generator to generate tensors where the values
    are clamped.

    Note: ``min_value`` and ``max_value`` cannot be both ``None``.

    Args:
        generator: The tensor generator or its configuration.
        min_value: The lower bound. If ``min_value`` is
            ``None``, there is no lower bound.
        max_value: The upper bound. If ``max_value`` is
            ``None``, there is no upper bound.

    Raises:
        ValueError: if both ``min`` and ``max`` are ``None``

    Example usage:

    ```pycon

    >>> from startorch.tensor import Clamp, RandUniform
    >>> generator = Clamp(RandUniform(low=1.0, high=50.0), min_value=2.0, max_value=10.0)
    >>> generator
    ClampTensorGenerator(
      (tensor): RandUniformTensorGenerator(low=1.0, high=50.0)
      (min_value): 2.0
      (max_value): 10.0
    )
    >>> generator.generate((2, 6))
    tensor([[...]])

    ```
    """

    def __init__(
        self,
        generator: BaseTensorGenerator | dict,
        min_value: float | None,
        max_value: float | None,
    ) -> None:
        super().__init__(generator=generator)
        if min_value is None and max_value is None:
            msg = "`min_value` and `max_value` cannot be both None"
            raise ValueError(msg)
        self._min_value = min_value
        self._max_value = max_value

    def __repr__(self) -> str:
        args = str_indent(
            str_mapping(
                {
                    "tensor": self._generator,
                    "min_value": self._min_value,
                    "max_value": self._max_value,
                }
            )
        )
        return f"{self.__class__.__qualname__}(\n  {args}\n)"

    def generate(self, size: tuple[int, ...], rng: torch.Generator | None = None) -> torch.Tensor:
        return self._generator.generate(size=size, rng=rng).clamp(self._min_value, self._max_value)


class DivTensorGenerator(BaseTensorGenerator):
    r"""Implement a tensor generator that divides one tensor by another
    one.

    This tensor generator is equivalent to:
        - ``output = dividend / divisor`` (a.k.a. true division)
        - ``output = dividend // divisor`` (a.k.a. floor division)

    Args:
        dividend: The dividend tensor generator or its
            configuration.
        divisor: The divisor tensor generator or its
            configuration.
        rounding_mode: The
            type of rounding applied to the result.
            - ``None``: true division.
            - ``"trunc"``: rounds the results of the division
                towards zero.
            - ``"floor"``: floor division.

    Example usage:

    ```pycon

    >>> from startorch.tensor import Div, RandUniform
    >>> generator = Div(RandUniform(), RandUniform(low=1.0, high=10.0))
    >>> generator
    DivTensorGenerator(
      (dividend): RandUniformTensorGenerator(low=0.0, high=1.0)
      (divisor): RandUniformTensorGenerator(low=1.0, high=10.0)
    )
    >>> generator.generate((2, 6))
    tensor([[...]])

    ```
    """

    def __init__(
        self,
        dividend: BaseTensorGenerator | dict,
        divisor: BaseTensorGenerator | dict,
        rounding_mode: str | None = None,
    ) -> None:
        super().__init__()
        self._dividend = setup_tensor_generator(dividend)
        self._divisor = setup_tensor_generator(divisor)
        self._rounding_mode = rounding_mode

    def __repr__(self) -> str:
        args = str_indent(str_mapping({"dividend": self._dividend, "divisor": self._divisor}))
        return f"{self.__class__.__qualname__}(\n  {args}\n)"

    def generate(self, size: tuple[int, ...], rng: torch.Generator | None = None) -> torch.Tensor:
        return self._dividend.generate(size=size, rng=rng).div(
            self._divisor.generate(size=size, rng=rng),
            rounding_mode=self._rounding_mode,
        )


class ExpTensorGenerator(BaseWrapperTensorGenerator):
    r"""Implement a tensor generator that computes the exponential of a
    tensor.

    This tensor generator is equivalent to: ``output = exp(tensor)``

    Example usage:

    ```pycon

    >>> from startorch.tensor import Exp, RandUniform
    >>> generator = Exp(RandUniform(low=1.0, high=5.0))
    >>> generator
    ExpTensorGenerator(
      (tensor): RandUniformTensorGenerator(low=1.0, high=5.0)
    )
    >>> generator.generate((2, 6))
    tensor([[...]])

    ```
    """

    def generate(self, size: tuple[int, ...], rng: torch.Generator | None = None) -> torch.Tensor:
        return self._generator.generate(size=size, rng=rng).exp()


class FmodTensorGenerator(BaseTensorGenerator):
    r"""Implement a tensor generator that computes the element-wise
    remainder of division.

    This tensor generator is equivalent to:
    ``output = dividend % divisor``

    Args:
        dividend: The tensor generator (or its configuration)
            that generates the dividend values.
        divisor: The divisor.

    Example usage:

    ```pycon

    >>> from startorch.tensor import Fmod, RandUniform
    >>> generator = Fmod(dividend=RandUniform(low=-100, high=100), divisor=10.0)
    >>> generator
    FmodTensorGenerator(
      (dividend): RandUniformTensorGenerator(low=-100.0, high=100.0)
      (divisor): 10.0
    )
    >>> generator.generate((2, 6))
    tensor([[...]])
    >>> generator = Fmod(
    ...     dividend=RandUniform(low=-100, high=100), divisor=RandUniform(low=1, high=10)
    ... )
    >>> generator
    FmodTensorGenerator(
      (dividend): RandUniformTensorGenerator(low=-100.0, high=100.0)
      (divisor): RandUniformTensorGenerator(low=1.0, high=10.0)
    )
    >>> generator.generate((2, 6))
    tensor([[...]])

    ```
    """

    def __init__(
        self,
        dividend: BaseTensorGenerator | dict,
        divisor: BaseTensorGenerator | dict | float,
    ) -> None:
        super().__init__()
        self._dividend = setup_tensor_generator(dividend)
        self._divisor = setup_tensor_generator(divisor) if isinstance(divisor, dict) else divisor

    def __repr__(self) -> str:
        args = str_indent(str_mapping({"dividend": self._dividend, "divisor": self._divisor}))
        return f"{self.__class__.__qualname__}(\n  {args}\n)"

    def generate(self, size: tuple[int, ...], rng: torch.Generator | None = None) -> torch.Tensor:
        tensor = self._dividend.generate(size=size, rng=rng)
        divisor = self._divisor
        if isinstance(divisor, BaseTensorGenerator):
            divisor = divisor.generate(size=size, rng=rng)
        tensor.fmod_(divisor)
        return tensor


class LogTensorGenerator(BaseWrapperTensorGenerator):
    r"""Implement a tensor generator that computes the logarithm of a
    tensor.

    This tensor generator is equivalent to: ``output = log(tensor)``

    Example usage:

    ```pycon

    >>> from startorch.tensor import Log, RandUniform
    >>> generator = Log(RandUniform(low=1.0, high=100.0))
    >>> generator
    LogTensorGenerator(
      (tensor): RandUniformTensorGenerator(low=1.0, high=100.0)
    )
    >>> generator.generate((2, 6))
    tensor([[...]])

    ```
    """

    def generate(self, size: tuple[int, ...], rng: torch.Generator | None = None) -> torch.Tensor:
        return self._generator.generate(size=size, rng=rng).log()


class MulTensorGenerator(BaseTensorGenerator):
    r"""Implement a tensor generator that multiplies multiple tensors.

    This tensor generator is equivalent to:
    ``output = tensor_1 * tensor_2 * ... * tensor_n``

    Args:
        generators: The tensor generators.

    Raises:
        ValueError: if no sequence generator is provided.

    Example usage:

    ```pycon

    >>> import torch
    >>> from startorch.tensor import Mul, RandUniform, RandNormal
    >>> generator = Mul([RandUniform(), RandNormal()])
    >>> generator
    MulTensorGenerator(
      (0): RandUniformTensorGenerator(low=0.0, high=1.0)
      (1): RandNormalTensorGenerator(mean=0.0, std=1.0)
    )
    >>> generator.generate((2, 6))
    tensor([[...]])

    ```
    """

    def __init__(self, generators: Sequence[BaseTensorGenerator | dict]) -> None:
        super().__init__()
        if not generators:
            msg = "No tensor generator. You need to specify at least one tensor generator"
            raise ValueError(msg)
        self._generators = tuple(setup_tensor_generator(generator) for generator in generators)

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}(\n  {str_indent(str_sequence(self._generators))}\n)"

    def generate(self, size: tuple[int, ...], rng: torch.Generator | None = None) -> torch.Tensor:
        output = self._generators[0].generate(size=size, rng=rng)
        for generator in self._generators[1:]:
            output.mul_(generator.generate(size=size, rng=rng))
        return output


class MulScalarTensorGenerator(BaseWrapperTensorGenerator):
    r"""Implement a tensor generator that multiplies a scalar value to a
    generated batch of tensors.

    This tensor generator is equivalent to:
    ``output = tensor * scalar``

    Args:
        generator: The tensor generator or its configuration.
        value: The scalar value to multiply.

    Example usage:

    ```pycon

    >>> import torch
    >>> from startorch.tensor import MulScalar, RandUniform, RandNormal
    >>> generator = MulScalar(RandUniform(), 42)
    >>> generator
    MulScalarTensorGenerator(
      (tensor): RandUniformTensorGenerator(low=0.0, high=1.0)
    )
    >>> generator.generate((2, 6))
    tensor([[...]])

    ```
    """

    def __init__(
        self,
        generator: BaseTensorGenerator | dict,
        value: float,
    ) -> None:
        super().__init__(generator=generator)
        self._value = value

    def __repr__(self) -> str:
        args = str_indent(str_mapping({"tensor": self._generator}))
        return f"{self.__class__.__qualname__}(\n  {args}\n)"

    def generate(self, size: tuple[int, ...], rng: torch.Generator | None = None) -> torch.Tensor:
        tensor = self._generator.generate(size=size, rng=rng)
        tensor.mul_(self._value)
        return tensor


class NegTensorGenerator(BaseWrapperTensorGenerator):
    r"""Implement a tensor generator that computes the negation of a
    generated tensor.

    This tensor generator is equivalent to: ``output = -tensor``

    Example usage:

    ```pycon

    >>> import torch
    >>> from startorch.tensor import Neg, RandNormal
    >>> generator = Neg(RandNormal())
    >>> generator
    NegTensorGenerator(
      (tensor): RandNormalTensorGenerator(mean=0.0, std=1.0)
    )
    >>> generator.generate((2, 6))
    tensor([[...]])

    ```
    """

    def generate(self, size: tuple[int, ...], rng: torch.Generator | None = None) -> torch.Tensor:
        return -self._generator.generate(size=size, rng=rng)


class SqrtTensorGenerator(BaseWrapperTensorGenerator):
    r"""Implement a tensor generator that computes the squared root of a
    tensor.

    This tensor generator is equivalent to: ``output = sqrt(tensor)``

    Example usage:

    ```pycon

    >>> from startorch.tensor import RandUniform, Sqrt
    >>> generator = Sqrt(RandUniform(low=1.0, high=100.0))
    >>> generator
    SqrtTensorGenerator(
      (tensor): RandUniformTensorGenerator(low=1.0, high=100.0)
    )
    >>> generator.generate((2, 6))
    tensor([[...]])

    ```
    """

    def generate(self, size: tuple[int, ...], rng: torch.Generator | None = None) -> torch.Tensor:
        return self._generator.generate(size=size, rng=rng).sqrt()


class SubTensorGenerator(BaseTensorGenerator):
    r"""Implement a tensor generator that subtracts two tensors.

    This tensor generator is equivalent to:
    ``output = tensor_1 - tensor_2``

    Args:
        tensor1: The first tensor generator or its
            configuration.
        tensor2: The second tensor generator or its
            configuration.

    Example usage:

    ```pycon

    >>> from startorch.tensor import RandNormal, RandUniform, Sub
    >>> generator = Sub(RandUniform(), RandNormal())
    >>> generator
    SubTensorGenerator(
      (tensor1): RandUniformTensorGenerator(low=0.0, high=1.0)
      (tensor2): RandNormalTensorGenerator(mean=0.0, std=1.0)
    )
    >>> generator.generate((2, 6))
    tensor([[...]])

    ```
    """

    def __init__(
        self, tensor1: BaseTensorGenerator | dict, tensor2: BaseTensorGenerator | dict
    ) -> None:
        super().__init__()
        self._tensor1 = setup_tensor_generator(tensor1)
        self._tensor2 = setup_tensor_generator(tensor2)

    def __repr__(self) -> str:
        args = str_indent(str_mapping({"tensor1": self._tensor1, "tensor2": self._tensor2}))
        return f"{self.__class__.__qualname__}(\n  {args}\n)"

    def generate(self, size: tuple[int, ...], rng: torch.Generator | None = None) -> torch.Tensor:
        return self._tensor1.generate(size=size, rng=rng).sub(
            self._tensor2.generate(size=size, rng=rng)
        )
