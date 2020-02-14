def main():
    num = int(input())
    for i in range(num):
        try:
            s = input()
            s_list = s.split()
            a = int(s_list[0])
            b = int(s_list[1])
            div = a/b
        except ZeroDivisionError:
            print('Error Code: делить на ноль нельзя')
            div = None
        except ValueError:
            print('Error Code: вы ввели странное значение вместо предполагаемых int и float')
            div = None
        print(f'a/b = {div}')


main()
