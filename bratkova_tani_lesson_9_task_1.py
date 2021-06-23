"""
1. Создать класс TrafficLight (светофор):
● определить у него один атрибут color (цвет) и метод running (запуск);
● атрибут реализовать как приватный;
● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
зелёный;
● продолжительность первого состояния (красный) составляет 7 секунд, второго
(жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
● переключение между режимами должно осуществляться только в указанном порядке
(красный, жёлтый, зелёный);
● проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
выводить соответствующее сообщение и завершать скрипт.
"""
# СОБСТВЕННОЕ РЕШЕНИЕ - Я так поняла условие задачи, что светофор переключается по кругу,
# и в следующий раз должен загореться не на красном, а с учетом того на котором
# остановился. Итак каждый раз, когда вызываем running(). Решение с урока разобрала -
# ниже закомментировано.

from time import sleep
from itertools import cycle


class TrafficLight:
    _next_color = 1  # эта переменная нужна, чтобы понять на коком цвете остановился светофор

    def __init__(self):
        self.__color = {1: ['Красный', 7], 2: ['Жёлтый', 2], 3: ['Зелёный', 4]}

    def running(self):
        print(f'{self.__color[TrafficLight._next_color][0]} '
              f'- ожидание {self.__color[TrafficLight._next_color][1]} сек')
        sleep(self.__color[TrafficLight._next_color][1])  # Сон в n секунд
        if TrafficLight._next_color == 3:
            TrafficLight._next_color = 1
        else:
            TrafficLight._next_color += 1


user1_traffic_light = TrafficLight()
print('\nМОЕ РЕШЕНИЕ - я так поняла условие задачи, что программа должна запоминать какой цвет был последний,'
      '\nи когда мы следующий раз вызываем running(), светофор должен загореться не с красного, а следующего по очереди')
how_many_times = int(input('Сколько раз переключить светофор? '))
for idx in range(how_many_times):
    user1_traffic_light.running()

# print(f'доступ к приватному атрибуту родительского класса '
#       f'my_traffic_light._TrafficLight__color {user1_traffic_light._TrafficLight__color}')

print('тут загорается светофор следующий по цвету после предыдущего, проверяем еще раз, вызвав running()')
user2_traffic_light = TrafficLight()
user2_traffic_light.running()


print('\nЭТО РЕШЕНИЕ С УРОКА')


class TrafficLightFromLesson:

    def __init__(self):
        self.__color = (('Red', 5), ('Yellow', 2), ('Green', 4))

    def running(self):
        for color, sec in cycle(self.__color):
            print(color, '(wait {} sec)'.format(sec))
            sleep(sec)


traffic_light_lesson = TrafficLightFromLesson()
traffic_light_lesson.running()
