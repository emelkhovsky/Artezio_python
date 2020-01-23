def processing(l):
    count = 0
    for element in l:
        if len(element) > 1 and element[0] == element[-1]:
            count += 1
    return count

l = ['abc', 'xyz', 'Aba', '1221']
result = processing(l)
print(result) #1