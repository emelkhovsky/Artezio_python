def processing(d):
    l = []
    for key, value in d.items():
        l.append(value)
    a1 = l[0]#самый большой
    a2 = 0
    a3 = 0
    for i in range(len(l)):
        if a1 < l[i]:
            a3 = a2
            a2 = a1
            a1 = l[i]
        elif a2 < l[i]:
            a3 = a2
            a2 = l[i]
        elif a1 < l[i]:
            a3 = l[i]

    return a1,a2,a3

d = {4: 16, 1: 1, 3: 9, 6: 36, 5: 25, 2: 4}
result = processing(d)
print(result) #(36, 25, 16)