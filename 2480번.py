num1, num2, num3 = map(int, input().split())

max = num1

if (num1 == num2 == num3):
	print(10000 + (num1 * 1000))
elif (num1 == num2):
	print(1000 + (num1 * 100))
elif (num2 == num3):
	print(1000 + (num2 * 100))
elif (num3 == num1):
	print(1000 + (num3 * 100))
else:
	if (num2 > max):
		max = num2
	if (num3 > max): 
		max = num3
	print(max * 100)