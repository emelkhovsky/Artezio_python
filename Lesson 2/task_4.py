def range_realization(n):
    range_list = []
    i = 0
    while i < n:
        range_list.append(i)
        i += 1
    return range_list

n = 4
rezult = range_realization(n)
print(rezult) #[0, 1, 2, 3]