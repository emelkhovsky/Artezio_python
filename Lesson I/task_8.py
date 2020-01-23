def processing(d):
    l = []
    for key, value in d.items():
        l.append(value)
    l.sort()
    return l[-1],l[-2],l[-3]

d = {4: 16, 1: 1, 3: 9, 6: 36, 5: 25, 2: 4}
result = processing(d)
print(result) #(36, 25, 16)