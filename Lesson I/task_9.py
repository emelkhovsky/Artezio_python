def processing(l):
    l_set = set(l)
    result = list(l_set)
    return result

l = [1, 2 ,5, 1, 1, 5, 7]
result = processing(l)
print(result) #[1, 2, 5, 7]