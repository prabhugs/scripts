a = [1,2,3,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
b = [1,1,1,3,2,4,5]


for i in range(1,10000000):
  a.sort()
  b.sort()

if a == b:
   print "yes"
else:
   print "no"
