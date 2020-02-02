def foo_recurtion(new_list, id_list, element):
    if type(element) != list and type(element) != tuple:
        id_list = []
        if element != 0:
            new_list.append(element)
    else:
        id_list.append(id(element))
        if len(set(id_list)) != len(id_list):
            print('обнаружена циклическая ссылка')
            return None
        for i in range(len(element)):
            rez = foo_recurtion(new_list, id_list, element[i])
            if not rez:
                return None
    return True

def foo(*args, **kwargs):
    new_list = []
    id_list = []
    rez = foo_recurtion(new_list, id_list, args)
    if not rez:
        return None
    for key in kwargs.keys():
        rez = foo_recurtion(new_list, id_list, kwargs[key])
        if not rez:
            return None
    sum = 0
    umn = 1
    for i in new_list:
        sum += i
        umn *= i
    return sum, umn

s = [1,2,3]
s.append(s)
rezult = foo(1, 2, [3, 4, (5, 6, 0)], a=(10, 11), b=(3, 4, [5, 6, [7, 8], []]))
print(rezult) #[1, 2, 3, 4, 5, 6, 10, 11, 3, 4, 5, 6, 7, 8] -> (75, 1596672000)
rezult = foo(1, 2, [3, 4, (5, 6, 0)], a=(10, 11), b=(3, 4, [5, s, [7, 8], []]))
print(rezult) #циклическая ссылка