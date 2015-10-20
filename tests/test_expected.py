import builtins
import getpass

import pytest

import prompt


class InputPatch():
    def __init__(self, monkeypatch):
        self.monkeypatch = monkeypatch

    def do(self, string):
        self.monkeypatch.setattr(builtins, "input", lambda prompt: string)
        self.monkeypatch.setattr(getpass, "getpass", lambda prompt: string)


@pytest.fixture
def input_patch(monkeypatch):
    return InputPatch(monkeypatch)


def test_character(input_patch):
    input_patch.do("c")
    assert prompt.character() == "c"


def test_email(input_patch):
    input_patch.do("foo@bar.not")
    assert prompt.email() == "foo@bar.not"


def test_integer(input_patch):
    input_patch.do("1")
    assert prompt.integer() == 1


def test_real(input_patch):
    input_patch.do("1.0")
    assert prompt.real() == 1.0


def test_regex(input_patch):
    import re
    response = "1. x=9"
    real_match = re.match(r"[0-9]\.\s([a-z])=([0-9])", response)
    input_patch.do(response)
    prompt_match = prompt.regex("[0-9]\\.\\s([a-z])=([0-9])")
    assert prompt_match is not None
    assert prompt_match.group() == real_match.group()
    assert prompt_match.groups() == real_match.groups()
    assert prompt_match.re == real_match.re
    assert prompt_match.span() == real_match.span()
    assert prompt_match.string == real_match.string


def test_secret(input_patch):
    input_patch.do("foo123")
    assert prompt.secret() == "foo123"


def test_string(input_patch):
    input_patch.do("foo123")
    assert prompt.string() == "foo123"
