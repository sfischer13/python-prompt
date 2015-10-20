import builtins
import getpass

import pytest

import prompt


@pytest.fixture(autouse=True)
def input_empty(monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda prompt: "")
    monkeypatch.setattr(getpass, "getpass", lambda prompt: "")


def test_character():
    assert prompt.character(empty=True) is None


def test_email():
    assert prompt.email(empty=True) is None


def test_integer():
    assert prompt.integer(empty=True) is None


def test_real():
    assert prompt.real(empty=True) is None


def test_regex():
    assert prompt.regex("foo", empty=True) is None


def test_secret():
    assert prompt.secret(empty=True) is None


def test_string():
    assert prompt.string(empty=True) is None
