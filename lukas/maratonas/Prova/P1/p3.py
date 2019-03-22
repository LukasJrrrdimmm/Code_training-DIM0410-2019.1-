while 1:
	n = input()
	if int(n) <= 0:
		break
	if int(n) <= 100:
		h = 1
		while(2**h < int(n)):
			h += 1
		b = 1
		f = 2**h
		c = 1
		print("Printing order from " + str(n) + " pages")
		while(b < f):
			#print(str(f) + " > " + n)
			if int(f) > int(n):
				print("Sheet " + str(c) + ", front: Blank, "+ str(b))
				b += 1
				f -= 1
			else:
				print("Sheet " + str(c) + ", front: " + str(f) + ", " + str(b))
				b += 1
				f -= 1
			#print(str(f) + " > " + n)
			if f == 0:
				break
			if f < b:
				break
			if int(f) > int(n):
				print("Sheet " + str(c) + ", back: " + str(b) + ", Blank")
				b += 1
				f -= 1
			else:
				print("Sheet " + str(c) + ", back: " + str(b) + ", " + str(f))
				b += 1
				f -= 1
			c+= 1
			
