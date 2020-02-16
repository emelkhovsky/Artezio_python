from time import sleep, time


class Counter(object):
    count_list = []

    @classmethod
    def counter(cls, time_value):
        cls.count_list.append(time_value)
        return cls.count_list


def average_time(n):
    def inner_decorator(function):
        def wrapper(*args, **kwargs):
            current_time = time()
            rezult = function(*args, **kwargs)
            t = time() - current_time
            values_list = Counter.counter(t)
            values_list = values_list[len(values_list) - n:]
            sum_values = 0
            for i in values_list:
                sum_values += i
            print(f'Среднее время работы: {int(sum_values/len(values_list)*1000)} мс.')
            return rezult
        return wrapper
    return inner_decorator


@average_time(n=2)
def foo(value):
    sleep(value)
    return value


foo(3)
foo(7)
foo(1)
