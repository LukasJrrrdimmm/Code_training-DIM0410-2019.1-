while 1:
	[n1, n2] = input().split(" ")
	if int(n1) == 0:
		break
	team = []
	team_result = []
	for i in range(0, int(n1)):
		team.append(input())
		team_result.append([team[i], 0, 0, 0, 0])
	for i in range(0, int(n2)):
		aux = input().split(" ")
		for j in range(0, int(n1)):
			a = []
			a = team_result[j]
			if aux[0] == a[0]:
				a[2] += 1
				a[3] += int(aux[1])
				a[4] += int(aux[3])
				if int(aux[1]) > int(aux[3]):
					a[1] += 3
				elif int(aux[1]) == int(aux[3]):
					a[1] += 1
			if aux[4] == a[0]:
				a[2] += 1
				a[3] += int(aux[3])
				a[4] += int(aux[1])
				if int(aux[3]) > int(aux[1]):
					a[1] += 3
				elif int(aux[3]) == int(aux[1]):
					a[1] += 1
			team_result[j] = a
	s1 = 0
	for j in range(0, len(team_result)):
		s1 += team_result[j][1]
		print(team_result[j])
	print(s1)
	
