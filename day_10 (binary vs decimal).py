"""
Task Given a base-10 integer, , convert it to binary (base-2). 
Then find and print the base-10 integer denoting the maximum number of consecutive 's in 's binary representation.
"""
# c = bin(int(input())).replace('0b', '')
# print(c)

def binary(decimal):
    otherBase = ""
    while decimal != 0:
        otherBase = str(decimal % 2) + otherBase   # todo Modulus: returns the remainder when first operand is divided by the second
        # print(otherBase)
        decimal //= 2   # todo Divide(floor) AND: Divide left operand with right operand and then assign the value(floor) to left operand
    return otherBase

print(binary(int(input())))

# print(sorted(list(map(len,'{0:b}'.format(n).split("0"))),reverse=True)[0])