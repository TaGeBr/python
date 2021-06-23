"""
Реализуйте базовый класс Car:
● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
● добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
● для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Вызовите методы и покажите результат.
"""

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала!')

    def stop(self):
        print(f'{self.name} остановилась!')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}!')

    def show_speed(self):
        print(f'{self.name} - текущая скорость {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Внимание! Превышена скорость 60 км/ч!!!')


class WorkCar(Car):
    def show_speed(self):
        print(f'{self.name} - текущая скорость {self.speed} км/ч')
        if self.speed > 40:
            print('Внимание! Превышена скорость 40 км/ч!!!')


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


town_car = TownCar(120, 'Серебристая', 'Городская машина', False)
work_car = WorkCar(90, 'Желтая', 'Рабочая машина', False)
sport_car = SportCar(420, 'Красная', 'Спортивная машина', False)
police_car = PoliceCar(180, 'Белая', 'Полицейская машина', True)

town_car.go()
town_car.stop()
town_car.turn('направо')
town_car.show_speed()
print()

work_car.go()
work_car.stop()
work_car.turn('налево во дворы')
work_car.show_speed()
print()

sport_car.go()
sport_car.stop()
sport_car.turn('в неизвестном направлении')
sport_car.show_speed()
print()

police_car.go()
police_car.stop()
police_car.turn('налево')
police_car.show_speed()
print()
