import pytest

from r_config import RConfig
from typing import Any


@pytest.fixture()
def rc() -> RConfig:
    return RConfig()


@pytest.fixture()
def yaml_str() -> str:
    return """
    yek:
      ramin: 2
      mehran: 'salam'
    # comment to test
    dow:
      se:
        p1: 2.2
      f1: 'khodafez'
    """


@pytest.fixture()
def r_dict() -> dict[str, Any]:
    return {'a': 10, 'b': 'example', 'f': {'p': 2, 'q': 3}}


def test_update_the_main_config(rc, yaml_str):
    rc.update_from_str(yaml_str)

    assert hasattr(rc, 'yek')


def test_from_dic(r_dict):
    rc = RConfig(r_dict)
    assert hasattr(rc, 'a')


def test_inner_dictionaries(r_dict):
    rc = RConfig(r_dict)
    assert isinstance(rc.f, RConfig)


def test_update_with_dictionary(rc, r_dict):
    rc.update(r_dict)
    assert hasattr(rc, 'a')
    assert rc.a == 10
    assert rc['a'] == 10
