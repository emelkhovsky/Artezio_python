def processing(s):
    s_dict = {}
    s_set = set(s)
    for element in s_set:
        s_dict[element] = s.count(element)
    return s_dict

s = 'google.com'
result = processing(s)
print(result) #{'g': 2, 'c': 1, 'o': 3, 'm': 1, 'e': 1, 'l': 1, '.': 1}
