=====================
Python Prompt Package
=====================

|PyPI Version| |Travis| |Coverage Status| |Documentation Status|

| Prompt and verify user input on the command line.
| Python 3.3+ and Wheels are supported.

The project was initiated by Stefan Fischer.

-  `Documentation <https://readthedocs.org/projects/prompt>`__ is
   available on PythonHosted.
-  `Questions <mailto:sfischer13@ymail.com>`__ can be asked via e-mail.
-  `Changes <https://github.com/sfischer13/python-prompt/blob/master/CHANGELOG.rst>`__
   between releases are documented.
-  `Source code <https://github.com/sfischer13/python-prompt>`__ is
   tracked on GitHub.
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

An extensive `documentation <https://readthedocs.org/projects/prompt>`__
is available.

Some simple use cases:

::

    import prompt

    email = prompt.email()

    # modify default prompt
    integer = prompt.integer(prompt="Please enter a number: ")

    # allow empty response
    real = prompt.real(empty=True)

    # require a two digit number using a regular expression
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

| Copyright (c) 2015-2017 Stefan Fischer
| The source code is available under the **MIT License**.
| See
  `LICENSE <https://github.com/sfischer13/python-prompt/blob/master/LICENSE>`__
  for further details.

.. |PyPI Version| image:: https://img.shields.io/pypi/v/prompt.svg
   :target: https://pypi.python.org/pypi/prompt
.. |Travis| image:: https://img.shields.io/travis/sfischer13/python-prompt.svg
   :target: https://travis-ci.org/sfischer13/python-prompt
.. |Coverage Status| image:: https://coveralls.io/repos/sfischer13/python-prompt/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/sfischer13/python-prompt?branch=master
.. |Documentation Status| image:: https://readthedocs.org/projects/prompt/badge/?version=latest
   :target: http://prompt.readthedocs.org/en/latest/?badge=latest
.. |PyPI Python Versions| image:: https://img.shields.io/pypi/pyversions/prompt.svg
   :target: https://pypi.python.org/pypi/prompt
.. |PyPI Wheel| image:: https://img.shields.io/pypi/wheel/prompt.svg
   :target: https://pypi.python.org/pypi/prompt
