import abc
from typing import Any, Generic, Sized, TypeVar

__version__ = "0.2.5.1"


SECRET_VALUE = "********"
EMPTY_VALUE = ""

T = TypeVar("T")


class _SecretField(Generic[T]):
    def __init__(self, v: T) -> None:
        self._v: T = v

    def get_secret_value(self) -> T:
        return self._v

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, self.__class__) and self._v == other._v

    def __str__(self) -> str:
        return str(self._display())

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({repr(self._display())})"

    @abc.abstractmethod
    def _display(self) -> T: ...


SizedT = TypeVar("SizedT", bound=Sized)


class SecretSized(_SecretField[SizedT]):
    def __len__(self):
        return len(self._v)


class SecretStr(SecretSized[str]):
    def __hash__(self) -> int:
        return hash(self._v)

    def _display(self):
        return SECRET_VALUE if self._v else EMPTY_VALUE


class SecretBytes(SecretSized[bytes]):
    def __hash__(self) -> int:
        return hash(self._v)

    def _display(self):
        return SECRET_VALUE.encode() if self._v else EMPTY_VALUE.encode()


class SecretStrList(SecretSized[list[str]]):
    def _display(self):
        return [SECRET_VALUE] if self._v else [EMPTY_VALUE]


class SecretBytesList(SecretSized[list[bytes]]):
    def _display(self):
        return [SECRET_VALUE.encode()] if self._v else [EMPTY_VALUE.encode()]
