i = int(input())
a = [i][i]
b = []
for c1 in range(0,i):
	s1 = 0
	s2 = 10000000
	for c2 in range(0,i):
		a[c1][c2] = int(input())
	for c2 in range(0,i):
		if s1 < a[c1][c2]:
			
