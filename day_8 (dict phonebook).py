"""
Given  names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. 
You will then be given an unknown number of names to query your phone book for. For each  queried, 
print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for  is not found, print Not found instead.
Note: Your phone book should be a Dictionary/Map/HashMap data structure.
"""
phoneBook = {}
for i in range(int(input())):
    key = input().strip()
    val = int(input())
    phoneBook[key]=val
while(True):
    k = str(input().strip())
    if k != None:
        if k in phoneBook:
            print(k + '=' + str(phoneBook[k]))
        else:
            print('Not found')
    else:
        break


phone = {}
n = int(input())
for i in range(0, n):
    name = str(input())
    phone[name] = str(input())
for i in range(0, n):
    name = str(input())
    re = phone.get(name, "none")
    if re!="none":
        print("%s=%s" % (name, re))
    else:
        print("Not found")


N = int(input())
book = []
tmp = [book.append([input(), int(input())]) for i in range(N)]
book = dict(book)

name = input()
while name!=None:
    number = book.get(name)
    if number != None:
        print(name + '=' + str(number))
    else:
        print('Not found')
    name = input()