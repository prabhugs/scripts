while True:
	try:
		string = raw_input()

		print string.capitalize()
		#print reduce(lambda x,y: x+' ' +y, map(lambda x: x[0].upper() + x[1:], string))
	except:
		break
