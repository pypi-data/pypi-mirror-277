import click

from conscia.secretvalue import SecretStr
from conscia.secretvalue.click_param import SecretStrParam


def test_click_param():
    assert SecretStrParam.convert("flaf", None, None) == SecretStr("flaf")
    assert SecretStrParam.convert(SecretStr("flaf"), None, None) == SecretStr("flaf")
    assert isinstance(SecretStrParam, click.ParamType)
