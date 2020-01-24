def processing(n):
    kol = 0
    for i in range(1,n+1):
        if i%2 == 1:
            print(i*i)
            kol +=1
    print('количество: ', kol)

n = 11
processing(n)


