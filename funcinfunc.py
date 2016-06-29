def m():
	a = {1:10, 2:20}
	def sub():
		#global a
		a[2] = 22
		print a
	sub()
m()
