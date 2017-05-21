def bitby (x):
	for i in range (0, 8, 1):
		a=x
		a = a >> i
		a = a & 1
		b = 1 << i
		print (b, ': \t',a)
