import itertools
cases = int(raw_input())

for i in xrange(cases):
    in_data = raw_input().split()
    
    x = 0
    a = int(in_data[0])
    b = int(in_data[1])
    c = int(in_data[2])
    k = int(in_data[3])
    
    print(next(x for x in xrange(100000) if(((a * (x**2)) + (b * x) + c) >= k)))
