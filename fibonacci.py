#!/usr/bin/env python3


def fibonacci(n):
    if n < 1:
        print("Parameter should be >= 1")
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


print(fibonacci(7))