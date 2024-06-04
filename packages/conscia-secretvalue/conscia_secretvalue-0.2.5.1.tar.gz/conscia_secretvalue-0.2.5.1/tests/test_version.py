import sys

if sys.version_info >= (3, 11):
    import tomllib

else:
    import tomli as tomllib

import conscia.secretvalue as secretvalue


def test_version():
    with open("pyproject.toml", "rb") as fp:
        proj = tomllib.load(fp)

    assert secretvalue.__version__ == proj["project"]["version"]
