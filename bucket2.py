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

			def executeSteps(sequence_list):
				interation = 0

				for i in xrange(len(sequence_list)):
					if big_container.weight == target or small_container.weight == target:
						break
					sequence_list[i]()

					if i == (len(sequence_list) -1):
						executeSteps(sequence_list)

					interation +=1
					if interation == 1000:
						break
				return

			def bigToSmall(target, big_container, small_container):
				approach1 = {'steps_taken':0}

				def seq1():
					while(big_container.weight >= small_container.size):
						big_init = big_container.weight
						big_container.transferTo(small_container)

						approach1['steps_taken'] += 1

						if big_container.weight == target or small_container.weight == target:
							break
						small_container.empty()
						approach1['steps_taken'] += 1

				def seq2():
					big_init = big_container.weight
					big_container.transferTo(small_container)

					approach1['steps_taken'] += 1

				def seq3():
					big_container.fill()
					approach1['steps_taken'] += 1

				sequence_list = [seq1, seq2, seq3]

				big_container.empty()
				small_container.empty()

				big_container.fill()
				approach1['steps_taken'] += 1

				executeSteps(sequence_list)

				return approach1


			def smallToBig(target, big_container, small_container):
				approach2 = {'steps_taken': 0}

				def seq1():
					while(big_container.weight != big_container.size):
						small_container.fill()
						approach2['steps_taken'] += 1
						print "Fill the " + str(small_container.size) + "L bucket with " + str(small_container.size) + "L of water"

						if big_container.weight == target or small_container.weight == target:
							break

						small_container_init = small_container.weight
						small_container.transferTo(big_container)
						approach2['steps_taken'] += 1
						print "Transfer the " + str(small_container.size) + "L bucket to" + str(big_container.size) + "L of water"


						if big_container.weight == target or small_container.weight == target:
							break

				def seq2():
					big_container.empty()
					approach2['steps_taken'] += 1
					print "Empty the " + str(big_container.size) + "L of water"

				def seq3():
					small_container_init = small_container.weight
					small_container.transferTo(big_container)

					approach2['steps_taken'] += 1
					print "Transfer the " + str(small_container.size) + "L bucket to" + str(big_container.size) + "L of water"

				sequence_list = [seq1, seq2, seq3]

				small_container.empty()
				big_container.empty()

				executeSteps(sequence_list)

				return approach2



			small_container = Container()
			big_container = Container()

			if container1 > container2:
				big_container.size = container1
				small_container.size = container2
			else:
				big_container.size = container2
				small_container.size = container1

			approach1 = bigToSmall(target, big_container, small_container) # big container to small
			approach2 = smallToBig(target, big_container, small_container) # small container to large


			print min(approach1['steps_taken'], approach2['steps_taken'])


calculateSteps(4, 5, 2)

#queries = int(raw_input())
#for query in xrange(queries):
#	container1 = int(raw_input())
#	container2 = int(raw_input())
#	target = int(raw_input())
#	calculateSteps(target, container1, container2)


