import dataclasses
import sys
from typing import Any, Generic, Sized, TypeVar

import pytest  # type: ignore

from conscia.secretvalue import SecretBytes, SecretBytesList, SecretSized, SecretStr, SecretStrList

SizedT = TypeVar("SizedT", bound=Sized)

if sys.version_info >= (3, 10):
    dataclass = dataclasses.dataclass
else:
    import typing_extensions

    @typing_extensions.dataclass_transform()
    def dataclass(*args: Any, slots: bool, kw_only: bool = False, **kwargs: Any):
        return dataclasses.dataclass(*args, **kwargs)


@dataclass(slots=True, kw_only=True)  # type: ignore
class Input(Generic[SizedT]):
    cls: type[SecretSized[SizedT]]
    value: SizedT
    other: SizedT
    want_str: str
    want_repr: str
    test_len: bool = True
    test_hash: bool = True


inputs: list[Input[Any]] = [
    Input(
        cls=SecretStr,
        value="flaf",
        other="oflaf",
        want_str="********",
        want_repr="SecretStr('********')",
    ),
    Input(
        cls=SecretBytes,
        value=b"flaf",
        other=b"oflaf",
        want_str="b'********'",
        want_repr="SecretBytes(b'********')",
    ),
    Input(
        cls=SecretStrList,
        value=["flaf"],
        other=["oflaf"],
        want_str="['********']",
        want_repr="SecretStrList(['********'])",
        test_hash=False,
    ),
    Input(
        cls=SecretBytesList,
        value=[b"flaf"],
        other=[b"oflaf"],
        want_str="[b'********']",
        want_repr="SecretBytesList([b'********'])",
        test_hash=False,
    ),
]


@pytest.mark.parametrize("cls,value,other", [(i.cls, i.value, i.other) for i in inputs if i.test_hash])
def test_hash(cls: type[SecretSized[SizedT]], value: SizedT, other: SizedT):
    s = cls(value)
    s_same = cls(value)
    s_other = cls(other)

    assert value != other, f"{value!r} != {other!r} [the two original values should differ]"
    assert hash(value) != hash(other)
    assert hash(s) == hash(s_same)
    assert hash(s) != hash(s_other)


@pytest.mark.parametrize("cls,value", [(i.cls, i.value) for i in inputs if i.test_len])
def test_len(cls: type[SecretSized[SizedT]], value: SizedT):
    s = cls(value)

    assert len(s) == len(value)


@pytest.mark.parametrize("cls,value,other", [(i.cls, i.value, i.other) for i in inputs if i.test_hash])
def test_equal(cls: type[SecretSized[SizedT]], value: SizedT, other: SizedT):
    s = cls(value)
    s_same = cls(value)
    s_other = cls(other)

    assert value != other, f"{value!r} != {other!r} [the two original values should differ]"
    assert s == s_same
    assert s != s_other


@pytest.mark.parametrize("cls,value,want", [(i.cls, i.value, i.want_str) for i in inputs if i.test_len])
def test_str(cls: type[SecretSized[SizedT]], value: SizedT, want: str):
    s = cls(value)

    assert str(s) == want


@pytest.mark.parametrize("cls,value,want", [(i.cls, i.value, i.want_repr) for i in inputs if i.test_len])
def test_repr(cls: type[SecretSized[SizedT]], value: SizedT, want: str):
    s = cls(value)

    assert repr(s) == want


@pytest.mark.parametrize("cls,value", [(i.cls, i.value) for i in inputs if i.test_len])
def test_get_secret(cls: type[SecretSized[SizedT]], value: SizedT):
    s = cls(value)

    assert s.get_secret_value() == value
