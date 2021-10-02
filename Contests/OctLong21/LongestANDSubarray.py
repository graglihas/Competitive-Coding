from math import pow,log2
for i in range(int(input())):
	n = int(input())
	power_of_2 = (int)(log2(n))
	multiple_of_2 = int(pow(2,power_of_2))
	a = n-multiple_of_2+1
	b = int(multiple_of_2/2)
	if a>=b:
		print(a)
	else:
		print(b)