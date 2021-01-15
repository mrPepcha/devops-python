#1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение
# ветофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep

class TrafficLight:
    __color = ['\033[31m\033[1m Красный', '\033[33m\033[1m Желтый', '\033[32m\033[1m Зеленый'] #добавим красок =)

    def running(self):
        i = 0
        while i < 3:
            print(f'\033[0m\033[6m Светофор переключается... \n '
                  f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(8)
            elif i == 2:
                sleep(3)
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()