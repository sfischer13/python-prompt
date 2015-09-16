# The MIT License (MIT)
#
# Copyright (c) 2015 Stefan Fischer
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""
This is a library for prompting input on the command line.

The package may be imported directly::

    import prompt

The library was initiated by Stefan Fischer and is developed and maintained by many others.
"""

import re

__author__ = "Stefan Fischer"
__contact__ = "Stefan Fischer <sfischer13@ymail.com>"
__copyright__ = "Copyright (c) 2015 Stefan Fischer"
__credits__ = []
__date__ = "2015-09-16"
__license__ = "MIT"
__status__ = "development"
__version__ = "0.1.0"

PROMPT = "? "


def character(prompt=None, empty=False):
    s = _prompt_input(prompt)
    if empty and not s:
        return None
    elif len(s) == 1:
        return s
    else:
        return character(prompt=prompt, empty=empty)


def integer(prompt=None, empty=False):
    s = _prompt_input(prompt)
    if empty and not s:
        return None
    else:
        try:
            return int(s)
        except ValueError:
            return integer(prompt=prompt, empty=empty)


def real(prompt=None, empty=False):
    s = _prompt_input(prompt)
    if empty and not s:
        return None
    else:
        try:
            return float(s)
        except ValueError:
            return real(prompt=prompt, empty=empty)


def regex(pattern, prompt=None, empty=False, flags=0):
    s = _prompt_input(prompt)
    if empty and not s:
        return None
    else:
        m = re.match(pattern, s, flags=flags)
        if m:
            return m
        else:
            return regex(pattern, prompt=prompt, empty=empty, flags=flags)


def string(prompt=None, empty=False):
    s = _prompt_input(prompt)
    if empty and not s:
        return None
    else:
        if s:
            return s
        else:
            return string(prompt=prompt, empty=empty)


def _prompt_input(prompt):
    if prompt is None:
        return input(PROMPT)
    else:
        return input(prompt)
