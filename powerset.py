#
#Python program to find the sum of power sets
#
from itertools import chain, combinations

n = 3
total=0
q = []

a = range(n)[1:]
a.append(n)

for i in range(1,n+1):
  q.append(combinations(a, i))

for i in q:
  total += reduce(lambda x,y:x+y, reduce(lambda x,y:x+y, i))

print total
