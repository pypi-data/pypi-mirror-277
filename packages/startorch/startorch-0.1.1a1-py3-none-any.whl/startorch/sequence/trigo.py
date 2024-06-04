r"""Contain the implementation of sequence generators that computes
trigonometric functions on sequences/tensors."""

from __future__ import annotations

__all__ = [
    "AcoshSequenceGenerator",
    "AsinhSequenceGenerator",
    "AtanhSequenceGenerator",
    "CoshSequenceGenerator",
    "SinhSequenceGenerator",
    "TanhSequenceGenerator",
]

from typing import TYPE_CHECKING

from startorch.sequence.wrapper import BaseWrapperSequenceGenerator

if TYPE_CHECKING:
    import torch


class AcoshSequenceGenerator(BaseWrapperSequenceGenerator):
    r"""Implement a sequence generator that computes the inverse
    hyperbolic cosine (arccosh) of each value.

    Example usage:

    ```pycon

    >>> import torch
    >>> from startorch.sequence import Acosh, RandUniform
    >>> generator = Acosh(RandUniform())
    >>> generator
    AcoshSequenceGenerator(
      (sequence): RandUniformSequenceGenerator(low=0.0, high=1.0, feature_size=(1,))
    )
    >>> generator.generate(seq_len=12, batch_size=4)
    tensor([[...]])

    ```
    """

    def generate(
        self, seq_len: int, batch_size: int = 1, rng: torch.Generator | None = None
    ) -> torch.Tensor:
        return self._generator.generate(seq_len=seq_len, batch_size=batch_size, rng=rng).acosh()


class AsinhSequenceGenerator(BaseWrapperSequenceGenerator):
    r"""Implement a sequence generator that computes the inverse
    hyperbolic sine (arcsinh) of each value.

    Example usage:

    ```pycon

    >>> import torch
    >>> from startorch.sequence import Asinh, RandUniform
    >>> generator = Asinh(RandUniform())
    >>> generator
    AsinhSequenceGenerator(
      (sequence): RandUniformSequenceGenerator(low=0.0, high=1.0, feature_size=(1,))
    )
    >>> generator.generate(seq_len=12, batch_size=4)
    tensor([[...]])

    ```
    """

    def generate(
        self, seq_len: int, batch_size: int = 1, rng: torch.Generator | None = None
    ) -> torch.Tensor:
        return self._generator.generate(seq_len=seq_len, batch_size=batch_size, rng=rng).asinh()


class AtanhSequenceGenerator(BaseWrapperSequenceGenerator):
    r"""Implement a sequence generator that computes the inverse
    hyperbolic tangent (arctanh) of each value.

    Example usage:

    ```pycon

    >>> import torch
    >>> from startorch.sequence import Atanh, RandUniform
    >>> generator = Atanh(RandUniform())
    >>> generator
    AtanhSequenceGenerator(
      (sequence): RandUniformSequenceGenerator(low=0.0, high=1.0, feature_size=(1,))
    )
    >>> generator.generate(seq_len=12, batch_size=4)
    tensor([[...]])

    ```
    """

    def generate(
        self, seq_len: int, batch_size: int = 1, rng: torch.Generator | None = None
    ) -> torch.Tensor:
        return self._generator.generate(seq_len=seq_len, batch_size=batch_size, rng=rng).atanh()


class CoshSequenceGenerator(BaseWrapperSequenceGenerator):
    r"""Implement a sequence generator that computes the hyperbolic
    cosine (cosh) of each value.

    Example usage:

    ```pycon

    >>> import torch
    >>> from startorch.sequence import Cosh, RandUniform
    >>> generator = Cosh(RandUniform())
    >>> generator
    CoshSequenceGenerator(
      (sequence): RandUniformSequenceGenerator(low=0.0, high=1.0, feature_size=(1,))
    )
    >>> generator.generate(seq_len=12, batch_size=4)
    tensor([[...]])

    ```
    """

    def generate(
        self, seq_len: int, batch_size: int = 1, rng: torch.Generator | None = None
    ) -> torch.Tensor:
        return self._generator.generate(seq_len=seq_len, batch_size=batch_size, rng=rng).cosh()


class SinhSequenceGenerator(BaseWrapperSequenceGenerator):
    r"""Implement a sequence generator that computes the hyperbolic sine
    (sinh) of each value.

    Example usage:

    ```pycon

    >>> import torch
    >>> from startorch.sequence import Sinh, RandUniform
    >>> generator = Sinh(RandUniform())
    >>> generator
    SinhSequenceGenerator(
      (sequence): RandUniformSequenceGenerator(low=0.0, high=1.0, feature_size=(1,))
    )
    >>> generator.generate(seq_len=12, batch_size=4)
    tensor([[...]])

    ```
    """

    def generate(
        self, seq_len: int, batch_size: int = 1, rng: torch.Generator | None = None
    ) -> torch.Tensor:
        return self._generator.generate(seq_len=seq_len, batch_size=batch_size, rng=rng).sinh()


class TanhSequenceGenerator(BaseWrapperSequenceGenerator):
    r"""Implement a sequence generator that computes the hyperbolic
    tangent (tanh) of each value.

    Example usage:

    ```pycon

    >>> import torch
    >>> from startorch.sequence import Tanh, RandUniform
    >>> generator = Tanh(RandUniform())
    >>> generator
    TanhSequenceGenerator(
      (sequence): RandUniformSequenceGenerator(low=0.0, high=1.0, feature_size=(1,))
    )
    >>> generator.generate(seq_len=12, batch_size=4)
    tensor([[...]])

    ```
    """

    def generate(
        self, seq_len: int, batch_size: int = 1, rng: torch.Generator | None = None
    ) -> torch.Tensor:
        return self._generator.generate(seq_len=seq_len, batch_size=batch_size, rng=rng).tanh()
