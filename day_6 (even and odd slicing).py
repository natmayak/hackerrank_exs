"""
Given a string, S, of length N that is indexed from 0 to N-1, print its even-indexed
and odd-indexed characters as 2 space-separated strings on a single line
"""

for N in range(int(input())):
    S = input()
    print(S[0::2], S[1::2])

# phrase = input('Give me some text: ')
# length = len(phrase)
#
# for number in range(0, length):
#     if number % 2 == 1:
#         print(phrase[number], end='')
# for number in range(0, length):
#     if number % 2 == 0:
#         print(phrase[number], end='')
