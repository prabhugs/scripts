cases = int(raw_input())

for i in xrange(cases):
    occur = int(raw_input())
    
    flist = {}
    plist = {}
    
    for j in xrange(occur):
	in_data = raw_input().split()
	
        if in_data[0] != in_data[1]:
            if in_data[0] not in flist:
              flist[in_data[0]] = 1

            else:
              flist[in_data[0]] = flist[in_data[0]] +1

            if in_data[1] in flist and flist[in_data[1]] > 0:
              flist[in_data[1]] = flist[in_data[1]] -1

            elif in_data[1] not in plist:
              plist[in_data[1]] = 1

            else:
              plist[in_data[1]] = plist[in_data[1]] +1
              #plist.append(in_data[1])

        #print ""
        #print in_data
        #print flist
        #print plist
        #print ""
    
    #print plist
    print sum(plist.values())

