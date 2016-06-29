cases = int(raw_input())

for i in xrange(cases):
  d1 = {}
  d2 = {}
  m = []
  f =[]
    
  status = 0
    
  indata = raw_input().split()
    
  for j in xrange(int(indata[1])):
	
    in_data = raw_input().split()
    in1 = in_data[0]
    in2 = in_data[1]
	
    if in1 not in m and in1 not in f:
      m.append(in1)
    if in2 not in m and in2 not in f:
        if in1 in m:
          f.append(in2)
        if in1 in f:
          m.append(in2)
    if (in1 in m and in2 in m) or (in1 in f and in2 in f):
          status = 1
	
  if status == 0:
    print "No suspicious lizards found!"
  else:
    print "Suspicious lizards found!"
