num1 = int(input())

num2 = 0
while (num2 < 10):
	num2 = num2 + 1
	print ("%d * %d = %d" %(num1, num2, num1*num2))
	
	if num2 == 9:
		break