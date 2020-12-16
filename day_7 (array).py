"""
Given an array, A, of N integers, print A's elements in
reverse order as a single line of space-separated numbers.
"""
from array import *

A = array('i', [])
for N in range(int(input())):
   A.append(int(input()))

for i in A[::-1]:
   print(i, end=" ")


#!/bin/python3

# import math
# import os
# import random
# import re
# import sys
# from array import *
#
#
# if __name__ == '__main__':
#     n = int(input())
#
#     arr = list(map(int, input().rstrip().split()))
#     print(" ".join(map(str, arr[::-1])))
# or
#     print(*arr[::-1])