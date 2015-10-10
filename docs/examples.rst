Usage Examples
==============

1. Ask for a floating point number:
    >>> prompt.real()
    ? 0.02
    0.02

2. The prompt may be customized:
    >>> prompt.integer(prompt="[0-9]+ ")
    [0-9]+ 42
    42

2. You can allow empty responses:
    >>> prompt.string(empty=True)
    ? <Enter>
    None

3. Ask for a password:
    >>> promp.secret(prompt="Enter your password: ")
    Enter your password: 
    '$uper$ecretP@ssw0rd'

3. Invalid responses will be rejected:
    >>> prompt.email()
    ? Bob.Miller
    ? bob@miller.foo
    'bob@miller.foo'

