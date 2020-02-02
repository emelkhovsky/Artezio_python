def sr_arifm(a,b,c,d):
    sr_ar = (a + b + c + d)/4
    global max_value
    global f
    max_current = max(a, b, c, d)
    if f == 0:
        max_value = max_current
        f = 1
    elif max_current > max_value:
            max_value = max(a,b,c,d)
    return sr_ar, max_value

f = 0
rezult = sr_arifm(1,2,3,4)
print(rezult) #(2.5, 4)
rezult = sr_arifm(-3, -2, 10, 1)
print(rezult) #(1.5, 10)
rezult = sr_arifm(7,8,8,1)
print(rezult) #(6.0, 10)