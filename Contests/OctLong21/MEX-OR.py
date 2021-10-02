from math import pow,log2
for i in range(int(input())):
	n = int(input())
	if n == 0:
		print(1)
	elif n == 1:
		print(2)
	else:
		power_of_2 = (int)(log2(n))
		a = int(pow(2,power_of_2))
		b = a*2
		if n+1 == b:
			print(b)
		else:
			print(a) 