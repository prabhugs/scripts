import timeit
import random

for i in range (10000, 100000, 20000):
  t = timeit.Timer("random.randrange(%d) in x"%i, "from __main__ import random, x")

  x = list(range(i))
  list_time = t.timeit(number = 1000)

  x = {j:None for j in range(i)}
  dict_time = t.timeit(number = 1000)

  print "Counter: " + str(i) + "  List: " + str(list_time) + "  Dict: " + str(dict_time)
