""""
Calculate the hourglass sum for every hourglass in 2D array, then print the maximum hourglass sum.
"""

import sys


arr = []
for arr_i in xrange(6):
   arr_temp = map(int,raw_input().strip().split(' '))
   arr.append(arr_temp)
max = -100
for i in range(4):
    for j in range(4):
        sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
        if max < sum:
            max = sum
print(max)

# making 2D array

# from array import *
# rows, cols = (5, 5)
# arr = [[0]*cols]*rows
# arr = [[0 for i in range(cols)] for j in range(rows)]
# print(arr)

# OR

# rows = int(input())
# cols = int(input())
# matrix = []
# for i in range(rows):
#   row = []
#   for j in range(cols):
#     row.append(0)
#   matrix.append(row)
# print(matrix)
