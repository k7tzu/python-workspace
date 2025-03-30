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

if __name__ == '__main__':
    import doctest
    doctest.testmod()