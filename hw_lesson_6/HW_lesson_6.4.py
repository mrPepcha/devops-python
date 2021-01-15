#4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} в движении'

    def stop(self):
        return f'{self.name} остановлена'

    def turn_right(self):
        return f'{self.name} поворачевает направо'

    def turn_left(self):
        return f'{self.name} поворачивает налево'

    def show_speed(self):
        return f'Текущая скорость {self.name} - {self.speed} км\ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городской машины {self.name} - {self.speed} км\ч')

        if self.speed > 40:
            return f'{self.name} превышает лимит скорости!'
        else:
            return f'{self.name} скорость в пределах нормы'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость рабочей машины {self.name} - {self.speed} км\ч')

        if self.speed > 60:
            return f'{self.name} превышает лимит скорости!'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} полицейская машина'
        else:
            return f'{self.name} не полицейская машина'


bmw = SportCar(110, 'Красный', 'Бэха', False)
solaris = TownCar(35, 'Желтый', 'Солярис', False)
gaz = WorkCar(90, 'Белый', 'ГАЗ', True)
lada = PoliceCar(70, 'Синий',  'Лада', True)
print(lada.turn_left())
print(solaris.turn_right(), ",", bmw.stop())
print(f'{gaz.go()} со скоростью {gaz.show_speed()}')
print(f'{gaz.name} {gaz.color} цвета')
print(f'{lada.name} полицейская машина? {lada.is_police}')
print(bmw.show_speed())
print(solaris.show_speed())
print(lada.police())
print(lada.show_speed())