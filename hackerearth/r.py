l1 = []
l2 = []
from collections import Counter

with open ("r", "r") as fp:
  for line in fp:
    a = line.split()
    l1.append(a[0])
    l2.append(a[1])

f= Counter(l1)
p= Counter(l2)

print sum((f-p).values())
print sum((p-f).values())
