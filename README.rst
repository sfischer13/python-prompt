Python Prompt Package
=====================

|PyPI Version| |PyPI Downloads| |Travis|

| This is a library for prompting input on the command line.
| Python 3.2+ and Wheels are supported.
| It was initiated by Stefan Fischer and is developed and maintained by
  many others.

-  `Questions <mailto:sfischer13@ymail.com>`__ can be asked via e-mail.
-  `Source code <https://github.com/sfischer13/python-prompt>`__ is
   tracked on GitHub.
-  `Changes <https://github.com/sfischer13/python-prompt/CHANGELOG.rst>`__
   between releases are documented.
-  `Bugs <https://github.com/sfischer13/python-prompt/issues>`__ can be
   reported on the issue tracker.

Install
-------

|PyPI Python Versions| |PyPI Wheel|

The package is available on
`PyPI <https://pypi.python.org/pypi/prompt>`__:

::

    $ pip install prompt

Use
---

The package may be imported directly:

::

    import prompt

    # modify default prompt
    integer = prompt.integer(prompt="Please enter a number: ")

    # allow empty response and return None
    real = prompt.real(empty=True)

    # require a two digit number
    regex = prompt.regex("^\d\d$")

Contribute
----------

| Write a bug report or send a pull request.
| Other
  `contributors <https://github.com/sfischer13/python-prompt/graphs/contributors>`__
  have done so before.

-  `Roadmap <https://github.com/sfischer13/python-prompt/blob/master/TODO.rst>`__
   of planned improvements
-  `Issues <https://github.com/sfischer13/python-prompt/issues>`__ that
   have been reported

License
-------

| Copyright (c) 2015 Stefan Fischer
| The source code is available under the **MIT License**.
| See
  `LICENSE <https://github.com/sfischer13/python-prompt/blob/master/LICENSE>`__
  for further details.

.. |PyPI Version| image:: https://img.shields.io/pypi/v/prompt.svg
   :target: https://pypi.python.org/pypi/prompt
.. |PyPI Downloads| image:: https://img.shields.io/pypi/dm/prompt.svg
   :target: https://pypi.python.org/pypi/prompt
.. |Travis| image:: https://img.shields.io/travis/sfischer13/python-prompt.svg
   :target: https://travis-ci.org/sfischer13/python-prompt
.. |PyPI Python Versions| image:: https://img.shields.io/pypi/pyversions/prompt.svg
   :target: https://pypi.python.org/pypi/prompt
.. |PyPI Wheel| image:: https://img.shields.io/pypi/wheel/prompt.svg
   :target: https://pypi.python.org/pypi/prompt
