cases = int(raw_input())

for i in xrange(cases):
  in_data = raw_input().split()
    
  x = 0
  while True:
    if ((int(in_data[0]) * (x**2)) + (int(in_data[1]) * x) + int(in_data[2])) >= int(in_data[3]):
      print x
      break
    x += 1
