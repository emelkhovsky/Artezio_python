def processing(s):
    result = 'Empty string'
    if len(s) > 1:
        result = s[:2] + s[-2:]
    return result

s1 = 'w3resource'
result = processing(s1)
print(result) #w3ce
s2 = 'w'
result = processing(s2)
print(result) #empty string