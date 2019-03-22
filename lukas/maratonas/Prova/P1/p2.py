while 1:
	n = input()
	if int(n) == 0:
		break
	arr = []
	for k in range(0, int(n)):
		arr.append(input().split())
	type_arr = []
	count = 0
	print(arr)
	num = -1
	last = []
	aux1 = []
	for k in range(0, len(arr)):
		flag = False
		counta = 0
		if len(type_arr) < 1:
			type_arr.append(arr[k])
			flag = True
			aux1 = arr[k]
		c = []
		aux2 = arr[k]
		print(aux2)
		print(type_arr)
		print()
		for j in range(0, len(type_arr)):
			counta = 0
			for m in range(0, len(aux1)):
				
				for l in range(0, len(aux2)):
					if int(type_arr[j][m]) == int(aux2[l]):
						counta += 1
			print(counta)
			if counta == len(aux2) - 1:
				flag = True
			else:
				c_add = 0
				
				for g in range(0, len(type_arr)):
					counta = 0
					for m in range(0, len(aux1)):
						
						for l in range(0, len(aux2)):
								if int(type_arr[j][m]) == int(aux2[l]):
									counta += 1
					print(counta)
					if aux2 == type_arr[g]:
						c_add += 1
					elif counta == len(type_arr[g]):
						c_add += 1
				print(c_add)
				if c_add == 0:
					type_arr.append(aux2)
		print(type_arr)
		print()
		aux1 = arr[k]
	last.append(type_arr)
	type_arr = []
	print("=============")
