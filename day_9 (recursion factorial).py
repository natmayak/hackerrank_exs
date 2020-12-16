# v.1
# import math
#
# print(math.factorial(int(input())))
#
# v.2

def factorial(n):
    if n == 1:
        return 1
    else:
        result = n * factorial(n - 1)
        print(n)
        return result

print(factorial(int(input())))