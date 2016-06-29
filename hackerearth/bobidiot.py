from string import maketrans
cases = int(raw_input())

zipped = []

for e in xrange(cases):
  zipped.append(raw_input().split())

string = raw_input()
in_string = string.lower()
out_string = in_string

print in_string
print "-----------"
print "-----------"

for entry in zipped:
  mychange = maketrans(entry[0].lower() + entry[1].lower(), entry[1].lower() + entry[0].lower())
  out_string = out_string.translate(mychange)
  print entry, out_string

print "-----------"
print out_string
case = [True if x.isupper() else False for x in string]
c = map(out_string, case)
print c
