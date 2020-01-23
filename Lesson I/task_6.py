def processing(n):
    new_dict = {}
    for i in range(1,n+1):
        new_dict[i] = i * i
    return new_dict

n = 6
result = processing(n)
print(result) #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}