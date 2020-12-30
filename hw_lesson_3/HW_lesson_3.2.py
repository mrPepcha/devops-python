#2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
def personal_func(name, lastname, byear, city, email, phone):
    print(name, lastname, byear, city, email, phone)

personal_func(name= 'alex', lastname='leverov', byear= 1990, city='Spb', email='bb@email.ru', phone='1234')