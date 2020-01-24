def authorization():
    f = 0
    while f == 0:
        print('Введите логин')
        login = input()
        print('Введите пароль')
        password = input()
        if password == 'cat':
            print(f'Password for user: {login} is correct')
            f = 1
        else:
            print(f'Password for user: {login} is incorrect')
            print('Please try again...')
            
authorization()