cases = int(raw_input())

for i in xrange(cases):
    occur = int(raw_input())
    
    flist = []
    plist = []
    
    for j in xrange(occur):
	in_data = raw_input().split()
	
        if in_data[0] != in_data[1]:
            flist.append(in_data[0])

            if in_data[1] in flist:
              flist.remove(in_data[1])
            else:
              plist.append(in_data[1])
    
    print len(plist)

