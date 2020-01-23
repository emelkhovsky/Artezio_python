def processing(d1, d2):
    for key in d1:
        if key not in d2:
            d2[key] = d1[key]
    return d2

d1 = {1:'1', 2:'2'}
d2 = {2:'2', 3:'3'}
result = processing(d1, d2)
print(result) #{2: '2', 3: '3', 1: '1'}