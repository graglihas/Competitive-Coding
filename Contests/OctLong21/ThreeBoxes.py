for i in range(int(input())):
	[A,B,C,D]=list(map(int,input().split()))
	if A+B+C <=D:
		print(1)
	elif A+B<=D or A+C<=D or B+C<=D:
		print(2)
	else:
		print(3)