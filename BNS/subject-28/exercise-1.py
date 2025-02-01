def fibonacci(n):
    """
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(25)
    75025
    """
    k = 0
    v = 1
    for _ in range(n):
        k, v = (k + v), k
    return k

if __name__ == "__main__":
    import doctest
    doctest.testmod()