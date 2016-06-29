a = "efbfkbvkjnbkjgnjlsngjlvsns"
lista = list(a)
if (len(lista) % 2 == 0 ):
    listb = lista[:(len(lista)/2)]
    listc = lista[(len(lista)/2):]

    if listb == list(reversed(listc)):
        print "yes"
    else:
        print "no"
else:
    listb = lista[:(len(lista)/2)]
    listc = lista[(len(lista)/2)+1:]

    if listb == list(reversed(listc)):
        print "yes"
    else:
        print "no"
