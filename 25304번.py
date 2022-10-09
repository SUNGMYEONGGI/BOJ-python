X = int(input())
N = int(input())
sum = 0

for prod in range(0, N):
    a, b = map(int, input().split())
    sum += a*b

    if N==0:
        break

if X==sum:
    print('YES')

else:
    print('No')