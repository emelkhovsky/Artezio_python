def main(k, v):
    a = {}
    [a.update({k[i]: v[i]}) if i < len(v) else a.update({k[i]: None}) for i in range(len(k))]
    return a


keys = ['a', 'b', 'c', 'd']
values1 = [1, 2, 3]
values2 = [1, 2, 3, 4, 5]
result = main(keys, values1)
print(result)
result = main(keys, values2)
print(result)