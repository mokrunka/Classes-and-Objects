def factorial(some_number):
    if some_number >= 2:
        return factorial(some_number - 1) * some_number
    else:
        return 1

print(factorial(5))