def sqrt_function(col):
    sqrt_list = []
    for el in col:
        sqrt_list.append(el ** 2)
    return sqrt_list

def chet_function(col):
    sqrt_list = []
    for i in range(len(col)):
        if i % 2 == 0:
            sqrt_list.append(col[i])
    return sqrt_list

def nechet_kub_function(col):
    sqrt_list = []
    for i in range(len(col)):
        if i % 2 == 1 and col[i] % 2 == 0:
            sqrt_list.append(col[i] ** 3)
    return sqrt_list


collection = [0,1,2,3,4,5,6,6]
print(sqrt_function(collection)) #[0, 1, 4, 9, 16, 25, 36, 36]
print(chet_function(collection)) #[0, 2, 4, 6]
print(nechet_kub_function(collection)) #[216]
