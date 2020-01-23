def processing(l1,l2):
    l1_set = set(l1)
    l2_set = set(l2)
    result = set.symmetric_difference(l1_set,l2_set)
    return result

l1 = [1, 2 ,5, 7]
l2 = [1, 2 ,13, 7]
result = processing(l1,l2)
print(result) #{5, 13}