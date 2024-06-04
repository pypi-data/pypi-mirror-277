from __future__ import annotations

import click  # type: ignore

from conscia.secretvalue import SecretStr


class _SecretStrParam(click.ParamType):
    name = "str"

    def convert(self, value: str | SecretStr, param: click.Parameter | None, ctx: click.Context | None):
        if isinstance(value, SecretStr):
            return value
        return SecretStr(value)


SecretStrParam = _SecretStrParam()
