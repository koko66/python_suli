def tre (sz,b):
	c=0
	h = len (sz)
	for i in range (0,h,1):
		if sz [i] == b:
			c+=1
	if c != 0:
		print (sz, "-ban van", c, "db", b)
	else:
		print ("nincs a(z) ", sz, "szóban", b, "betű")
