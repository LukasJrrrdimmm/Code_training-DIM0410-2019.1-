import math as m
while 1:
	try:
		n = int(input())
		#if n >= 1:
		if n <= (10**5):
			l = 0
			count = 0
			while 1:
				k = 1
				f = 1
				while n > 0:
					f *= k
					k += 1
					if f > n:
						count += 1
						n -= f/(k-1)
						break
				if n <= 0:
					print(count)
					break
	except EOFError:
		break
