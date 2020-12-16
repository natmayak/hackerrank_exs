
n = int(input('enter the number of stones: '))
s = input('enter their colours: ')
i = 0
max_len = len(s) - 1
stones_to_remove = 0
for elem in s:
    if i < max_len and s[i] == s[i + 1]:
        print('two equal neighbours found')
        stones_to_remove += 1
    else:
        pass
    i+=1

print(stones_to_remove)

# while n < max_len:
#         if a[n] == a[n + 1]:
#             print('two equal neighbours found')
#         else:
#             pass
#         n+=1
