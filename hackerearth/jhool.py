cases = int(raw_input())

for i in xrange(cases):
  chances = int(raw_input().split()[1])
  status = "YES"
  l = []
  for j in xrange(chances):
    in_data = raw_input().split()
    in1 = int(in_data[0])
    in2 = int(in_data[1])


    if in1 < in2:
      #r = range(in1, in2)
      ll = [x for x in xrange(in1, in2)]
      l.extend(ll)
      l.append(in2)
      #print l

    if in1 == in2:
      ll = [x for x in xrange(in1, in2)]
      #l.append(in1)
      #l.append(in2)
      l.extend(ll)
      #print l
      #status = "NO"
  print l
  #print status
