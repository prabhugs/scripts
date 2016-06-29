cases = int(raw_input())
     
for case in xrange(cases):
	entry = int(raw_input())
    	
	a = {}
	b = {}
    
	l1 = raw_input().split()
	l2 = raw_input().split()
    	
	o = [0]
	sl1 = set(l1)
	sl2 = set(l2)
    	
	for i in l2:
		if i in l1:
			o.append(int(l2.index(i)) - int(l1.index(i)))
print max(o)
