in_data = raw_input().split()

num_dino = int(in_data[0])
num_tuple = int(in_data[1])
max_tup_val = int(in_data[2])
num_quest = int(in_data[3])

dino_dict = {}


for i in xrange(num_dino):
    this_dino = raw_input()
    tdino = this_dino.split()
    #k = int(''.join(tdino[-num_tuple:]))
    k = '.'.join(tdino[-num_tuple:])
    dino_dict[k] = tdino[0]
    
for i in xrange(num_quest):
    #quest = int(''.join(raw_input().split()))
    quest = '.'.join(raw_input().split())
    if quest in dino_dict:
	print dino_dict[quest]
    else:
	print "You cant fool me :P"
