class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        self.maximumDifference = max(self.__elements) - min(self.__elements)

# def computeDifference(self):
#         self.maximumDifference = max(abs(a - b) for a in self.__elements for b in self.__elements)

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)