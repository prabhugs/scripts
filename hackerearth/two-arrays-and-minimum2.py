data = map(int, raw_input().split())

a = data[0]
b = data[1]
c = data[2]

count = int(raw_input())

lista = []
listb = []

lista.append(a * c)
listb.append(b * c)

for x in xrange(1, count):
	lista.append(((lista[x-1] * a * b * c) + (lista[x-1] * a * b) + (lista[x-1] * a * c)) % 1000000007)
	
for x in xrange(1, count):
	listb.append(((listb[x-1] * a * b * c) + (listb[x-1] * a * b) + (listb[x-1] * b * c)) % 1000000007)

#lista = sorted(lista)
#listb = sorted(listb)

#lista.sort()
#listb.sort()

#a1 = lista[0] + listb[1]
#a2 = lista[1] + listb[0]

print min(lista)
print min(listb)

print lista.index(min(lista))
print listb.index(min(listb))
#print min(a1, a2)

