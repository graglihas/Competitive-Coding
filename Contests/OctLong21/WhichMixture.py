for i in range(int(input())):
	[A,B]=list(map(int,input().split()))
	if B == 0:
		print("Solid")
	elif A==0:
		print("Liquid")
	else:
		print("Solution")