in_data = raw_input().split()

users = int(in_data[0])
queries = int(in_data[1])

leader_board = {x:0 for x in xrange(1, users+1)}

for q in xrange(queries):
  data = raw_input().split()
  user, cur_score = int(data[0]), int(data[1])
  
  leader_board[user] = leader_board[user] + cur_score
  
  #o = sorted(leader_board.values(), reverse=True)
  o = leader_board.values()
  o.sort(reverse=True)
    
  summed = 0
  for e in o:
    summed += e * (o.index(e) +1)
  print summed
