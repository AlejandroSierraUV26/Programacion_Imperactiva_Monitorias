# def mystery_function(x, y):
#     if x == 0:
#         return y
#     else:
#         return mystery_function(x - 1, x + y)

# result = mystery_function(3, 2)
# print(result)
# """
# A) 2
# B) 7
# C) 6
# D) 8
# """










# def arithmetic_operation(x, y):
#     result = (x + y) * (x - y) / 2
#     return result

# x = 6
# y = 4
# output = arithmetic_operation(x, y)
# print(output)

"""
A) 10.0
B) 14.0
C) 20.0
D) 16.0
"""


# def calculate_power(x, n):
#     if n == 0:
#         return 1
#     else:
#         result = x
#         for i in range(1, n):
#             result = result * x
#         return result

# x = 2
# n = 3
# output = calculate_power(x, n)
# print(output)


# """
# A) 2
# B) 4
# C) 6
# D) 8
# """


def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= n
    return result

n = 5
recursive_result = factorial_recursive(n)
iterative_result = factorial_iterative(n)

print("Factorial de", n, "usando recursión:", recursive_result)
print("Factorial de", n, "usando iteración:", iterative_result)


# """
# A) 20
# B) 15
# C) 120
# D) 25
# """
