#1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
# года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
#from datetime import date
class Date:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f'Все в порядке'
                else:
                    return f'Неправильный год (возможно от 0 до 2021)'
            else:
                return f'Неправильный месяц (возможно от 1 до 12)'
        else:
            return f'Неправильный день (возможно от 1 до 31)'

    def __str__(self):
        return f'Текущая дата: {Date.extract(self.day_month_year)}'


today = Date('22 - 01 - 2021')
print(today)
print(today.valid(11, 11, 2022))
print(today.extract('11 - 11 - 2020'))
print(Date.valid(12, 13, 2030))