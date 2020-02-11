class Student(object):

    def __init__(self, name, info_dict):
        self.name = name
        self.info_dict = info_dict
        self.sum = 0
        self.points = [0] * self.info_dict.get('lab_num')  # список баллов за каждую лабу
        self.attempts = [0] * self.info_dict.get('lab_num')  # список попыток за каждую лабу соответственно

    def make_lab(self, m, n=0):
        if 0 <= n < self.info_dict.get('lab_num') - 1:
            if 0 < m <= self.info_dict.get('lab_max'):
                if self.attempts[n] < 3:  # ограничение в 3 попытки
                    self.points[n] = m
                    self.attempts[n] += 1
        return self

    def make_exam(self, m):
        if 0 < m <= self.info_dict.get('exam_max'):
            self.sum += m
        return self

    def is_sertified(self):
        for i in self.points:
            self.sum += i
        rez = True
        if self.sum / 100 < self.info_dict.get('k'):
            rez = False
        return self.name, self.sum, rez


def main():
    student_name = 'Vlad'
    course_info = {'exam_max': 30, 'lab_max': 7, 'lab_num': 10, 'k': 0.61}
    vlad = Student(student_name, course_info)
    vlad.make_lab(6, 2)
    vlad.make_lab(5, 3)
    vlad.make_lab(7, 3)
    vlad.make_lab(7, 4)
    vlad.make_lab(6)
    vlad.make_lab(6)
    vlad.make_lab(6)
    vlad.make_lab(6)  # Четвертая попытка уже не учитывается
    vlad.make_lab(6, 8)
    vlad.make_lab(7, 5)
    vlad.make_exam(30)
    rez = vlad.is_sertified()
    return rez


rezult = main()
print(rezult)
