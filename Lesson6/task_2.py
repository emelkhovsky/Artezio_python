def main(a_object):
    b = [i for i in dir(a_object) if not i.startswith('_')]
    return b


a = 'student'
rezult = main(a)
print(rezult)
