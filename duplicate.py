a = [1,1,2,2,2,3,4,5]
c=[]
d=[]

for entry in a:
    if entry not in c:
        c.append(entry)
        d.append(entry)
        print "----"
        print c
        print d
        print "----"
        pass
    if entry in c and entry in d:
        print d
        d.remove(entry)
print c
print d
