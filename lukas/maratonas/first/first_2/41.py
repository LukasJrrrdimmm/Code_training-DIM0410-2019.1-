it = 0
while 1:
	it += 1
	try:
		n = int(input())
		blank = input()
		if n != 0:
			print()
			r1 = []
			sp = []
			sp_count = []
			while 1:
				try:
					a = input()
					flag = False
					if len(sp) == 0:
						sp.append(a)
						sp_count.append(1)
					else:
						for i in range(0, len(sp)):
							if(a == sp[i]):
								flag = False
								sp_count[i] += 1
								break
							else:
								flag = True
						if flag == True:
							sp.append(a)
							sp_count.append(1)
				except EOFError:
					if len(sp) == 0:
						break
					else:
						s = 0
						pct = []
						c1 = "0"
						for i in range(0, len(sp_count)):
							s += sp_count[i]
						for i in range(0, len(sp_count)):
							pct.append((float(sp_count[i])/float(s))*100)
						while(len(r1) < len(sp)):
							c = "Zzzzzzzzzzzz"
							p = 0
							for i in range(0, len(sp)):
								if(sp[i] < c) & (sp[i] > c1):
									c = sp[i]
									p = pct[i]
							c1 = c
							r1.append([c1, p])
						for i in range(0, len(r1)):
							print("{} {:.4f}".format(str(r1[i][0]) ,float(r1[i][1])))
						break
				
	except EOFError:
		break
	if it == 2:
		it = 0
		print()
