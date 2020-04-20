
from collections import OrderedDict
words = OrderedDict()
n=int(input())
for _ in range(n):
    element = input()
    words.setdefault(element, 0)
    words[element] += 1
   
print(len(words))
print(*words.values())

