from itertools import groupby

def string_groupby():
  a = "prabhu gnana sundar"
  b = list(a)
  b.sort()
  print b
  for x,y in groupby(b):
    listy = list(y)
    print x, len(listy), listy

def file_groupby():

  contents = ''
  para_num = 0
  sorted_lines = []
  keyword = "license"
  keyword_list = ["license", "lisense", "licence"]
  keyword_count = 0

  with open('license.txt', 'rb') as infile:
    contents = infile.readlines()
    for line in contents:
      linelist = line.split()
      linelist.sort()
      sorted_lines.append(linelist)
      enum_lines = enumerate(sorted_lines, 1)
  #print len(contents)
  #print len(sorted_lines)
  #print sorted_lines
  for linenum, line in enum_lines:
    for elt, items in groupby(line):
      if elt.lower().find(keyword) != -1:
        l = len(list(items))
      #if l > 1:
        print elt, linenum 
  print len(sorted_lines)

def test():
  a = ['0\n', '0.0', '0.0', '1', '10', '1144531', '120', '150.0', '2016-02-03 06:43:56.000', '2016-02-03 06:44:42.000', '23.36261', '27.9', '304.0', '591.0', '73.464937', 'A', 'LF102115', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'P1', 'Trimble']
  for x,y in groupby(a):
    listy = list(y)
    print x, len(listy), listy

if __name__ == "__main__":

  #string_groupby()

  file_groupby()
  #test()



