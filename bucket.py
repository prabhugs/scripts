from fractions import gcd

def calculateSteps(target, container1, container2):
	if target > container1 and target > container2:
		print -1
	else:
		if target % gcd(container1, container2) != 0:
			print -1
		else:
			result = {}

			class Container:
				def __init__(self):
					self.weight = 0
					self.size = 0

				def fill(self):
					self.weight = self.size

				def empty(self):
					self.weight = 0

				def transferTo(self, other_container):
					if(self.weight > other_container.size - other_container.weight):
						self.weight -= other_container.size - other_container.weight
						other_container.weight = other_container.size
					else:
						other_container.weight += self.weight
						self.empty()

			def runSequence(sequence):
				cycle = 0

				for i in xrange(len(sequence)):
					if big_container.weight == target or small_container.weight == target:
						break
					sequence[i]()

					if i == (len(sequence) -1):
						runSequence(sequence)

					cycle +=1
					if cycle == 1000:
						break
				return

			def First(target, big_container, small_container):
				first = {'count':0}

				def seq1():
					while(big_container.weight >= small_container.size):
						big_init = big_container.weight
						big_container.transferTo(small_container)

						big_diff = big_init - big_container.weight
						first['count'] += 1

						if big_container.weight == target or small_container.weight == target:
							break
						small_container.empty()
						first['count'] += 1

				def seq2():
					big_init = big_container.weight
					big_container.transferTo(small_container)

					big_diff = big_init - big_container.weight
					first['count'] += 1

				def seq3():
					big_container.fill()
					first['count'] += 1

				sequence = [seq1, seq2, seq3]

				big_container.empty()
				small_container.empty()

				big_container.fill()
				first['count'] += 1

				runSequence(sequence)

				return first


			def Second(target, big_container, small_container):
				second = {'count': 0}

				def seq1():
					while(big_container.weight != big_container.size):
						small_container.fill()
						second['count'] += 1
						print "Fill the " + str(small_container.size) + "L bucket with " + str(small_container.size) + "L of water"

						if big_container.weight == target or small_container.weight == target:
							break

						small_container_init = small_container.weight
						small_container.transferTo(big_container)
						second['count'] += 1
						print "Transfer the " + str(small_container.size) + "L bucket to " + str(big_container.size) + "L of water"

						small_container_diff = small_container_init - small_container.weight

						if big_container.weight == target or small_container.weight == target:
							break

				def seq2():
					big_container.empty()
					second['count'] += 1
					print "Empty the " + str(big_container.size) + "L of water"

				def seq3():
					small_container_init = small_container.weight
					small_container.transferTo(big_container)

					small_container_diff = small_container_init - small_container.weight
					second['count'] += 1

				sequence = [seq1, seq2, seq3]

				small_container.empty()
				big_container.empty()

				runSequence(sequence)

				return second



			small_container = Container()
			big_container = Container()

			if container1 > container2:
				big_container.size = container1
				small_container.size = container2
			else:
				big_container.size = container2
				small_container.size = container1

			first = First(target, big_container, small_container) # large to small
			second = Second(target, big_container, small_container) # small to large


			print first
			print second
			print min(first['count'], second['count'])


calculateSteps(5, 2, 3)

#
## Uncomment below lines to accept input from external source
#
#queries = int(raw_input())
#for query in xrange(queries):
#	container1 = int(raw_input())
#	container2 = int(raw_input())
#	target = int(raw_input())
#	calculateSteps(target, container1, container2)
#
