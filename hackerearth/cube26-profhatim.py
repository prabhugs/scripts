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
    in1 = int(in_data[0])
    in2 = int(in_data[1])
	
    if (in1 in d1 and in2 in d1) or (in1 in d2 and in2 in d2):
    elif in1 not in d1 and in1 not in d2:
      if in2 not in d1:
        d1[in1] = in2
        d2[in2] = in1
      else:
        d2[in1] = in2

    elif in1 in d1 and not in d2:
      if in2 not in d2:
        d2[in2] = in1
      elif in2 in d1:
        status = 1

    elif in1 in d2:
      if in2 not in d1:
        d1[in2] = in1
      elif in2 in d2:
        status = 1 

    #elif in2 not in d1 and in2 not in d2:
    #    if in1 in d1:
    #      d2[in2] = in1
    #    if in1 in d2:
    #      d1[in2] = in1
#    elif (in1 in d1 and in2 in d1) or (in1 in d2 and in2 in d2):
#          print "-----------------------"
#          print in1, in2
#          print d1
#          print d2
#          print "-----------------------"
#          status = 1
	
  if status == 0:
    print "No suspicious lizards found!"
  else:
    print "Suspicious lizards found!"
