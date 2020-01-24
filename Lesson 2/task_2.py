def processing(a,b,c):
    kol = 0
    for i in range(a+1,b):
        if i%c == 0:
            kol +=1
    return kol

a = 10
b = 20
c = 3
rezult = processing(a,b,c)
print(rezult)#3