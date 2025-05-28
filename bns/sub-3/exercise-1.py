def fibonacci(n):
    """
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(25)
    75025
    """
    x, y = 0, 1
    for i in range(n):
        x, y = y, x + y
    return x

def fibo_recursion(n):
    """
    >>> fibo_recursion(1)
    1
    >>> fibo_recursion(2)
    1
    >>> fibo_recursion(25)
    75025
    """
    if n <= 1:
        return n
    else:
        return (fibo_recursion(n-1) + fibo_recursion(n-2))

if __name__ == '__main__':
    import doctest
    doctest.testmod()