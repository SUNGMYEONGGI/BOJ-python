num1 = int(input())
NUM = num1
count = 0

while True:
    a = ((num1 // 10) + (num1 % 10)) % 10
    N = ((num1 % 10) * 10) + a
    num1 = N
    count += 1

    if num1 == NUM:
        break

print(count)