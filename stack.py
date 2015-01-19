import pdb

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

def revstring(str):
  s = Stack()
  ss = ''
  l = len(str) -1
  while l >= 0:
    s.push(str[l])
    l-=1
    print  ss, s.peek()
    ss = ss + s.peek()
  return ss

#print revstring("prabhu")
