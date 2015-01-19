from stack import Stack

def convertToBinary(value):
  remainder = Stack()

  while value > 0:
    rem = value % 2
    remainder.push(rem)
    value = value // 2

  binary = ''
  while not remainder.isEmpty():
    binary = binary + str(remainder.pop())
  
  return binary

def myconvertTobinary(value):
  remainder = Stack()

  while value > 0:
    rem = value % 8
    remainder.push(rem)
    value = value // 8

  binary = ''
  while not remainder.isEmpty():
    binary = binary + str(remainder.pop())

  return binary


print convertToBinary(43)
print myconvertTobinary(25)
