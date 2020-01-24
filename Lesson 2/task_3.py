def processing(n):
    if n == 1 or n == 0:
        return 1
    fact = 1
    for i in range(2,n+1):
        fact *= i
    return fact

n = 4
rezult = processing(n)
print(rezult) #24