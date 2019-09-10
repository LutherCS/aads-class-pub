#!/usr/bin/env python3
# encoding: UTF-8
"""
@author: Roman Yasinovskyy
@date: 2019
@module: notes.environment
"""

import pathlib
import pytest
import toml
from src.notes.environment.hello import hello

THIS_DIR = pathlib.Path(".")
TEST_DIR = pathlib.Path("tests/notes/environment/")
FILE_PUBLIC = pathlib.Path("test_hello_public.toml")
FILE_SECRET = pathlib.Path("test_hello_secret.toml")

if "tests" not in THIS_DIR.parts:
    FILE_PUBLIC = THIS_DIR / TEST_DIR / FILE_PUBLIC
    FILE_SECRET = THIS_DIR / TEST_DIR / FILE_SECRET

all_test_cases = toml.load(FILE_PUBLIC)

TIME_LIMIT = 1
AUDIENCE = [
    (v.get("data"), v.get("expected"))
    for v in all_test_cases.get("case_public").get("success").values()
]
AUDIENCE_ERR = [
    (v.get("data", None), v.get("expected", None))
    for v in all_test_cases.get("case_public").get("error").values()
]
if FILE_SECRET.exists():
    all_test_cases.update(toml.load(FILE_SECRET))
    AUDIENCE.extend(
        [
            (v.get("data"), v.get("expected"))
            for v in all_test_cases.get("case_secret").get("success").values()
        ]
    )
    AUDIENCE_ERR.extend(
        [
            (v.get("data", None), v.get("expected", None))
            for v in all_test_cases.get("case_secret").get("error").values()
        ]
    )


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("data, expected", AUDIENCE)
def test_hello(data, expected):
    """Testing the output"""
    assert hello(data) == expected


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("data, expected", AUDIENCE_ERR)
def test_hello_err(data, expected):
    """Testing the exception"""
    with pytest.raises(TypeError) as exc:
        hello(data)
    assert str(exc.value) == expected


if __name__ == "__main__":
    pytest.main(["-v", "test_hello.py"])
