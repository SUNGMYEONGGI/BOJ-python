def factorial(n):
    i = 1
    if n == 0:
        return 1
    else:
        i = n * factorial(n - 1)
        return i
    
a = int(input())
print(factorial(a))