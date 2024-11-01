print("Sarah on top <3")

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    a, b = 1, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b

print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(25))