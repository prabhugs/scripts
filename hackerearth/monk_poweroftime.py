a = [1,2,3,4,5]

b = [2,3,1,4,5]

a = [3,2,1]
b = [1,3,2]
change = 0

def r(a, b, pos):
	global change
	if a == b:
		print a,b, len(a), change
		return change+len(a)
	if pos < len(a): 
		if a[pos] == b[pos]:
			change += 1
			print a, b, pos, change
			r(a,b,pos+1)
		else:
			print a, b, pos, change
			d = a.pop(pos)
			a.append(d)
			change += 1
			r(a,b,pos)

	return change

print r(a,b,0)
