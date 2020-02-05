import website_alive.check_response as check_module


def processing():
    s = input('введите адрес сайта')
    if check_module.check(s):
        print('сайт жив')
    else:
        print('сайт умер')


processing()
