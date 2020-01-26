def range_realization(*args):
    range_list = []
    step = 1
    i = 0
    limit = args[0]
    len_args = len(args)
    if len_args == 2:
        i = args[0]
        limit = args[1]
    elif len_args == 3:
        i = args[0]
        step = args[2]
        limit = args[1]
    while i < limit:
        range_list.append(i)
        i += step
    return range_list

rezult = range_realization(4,10)
print(rezult) #[4, 5, 6, 7, 8, 9]
rezult = range_realization(10)
print(rezult) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
rezult = range_realization(4,10,2)
print(rezult) #[4, 6, 8]
