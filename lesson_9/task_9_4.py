class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} начинает движение!')

    def stop(self):
        print(f'{self.name} тормозит!')

    def turn(self, direction):
        print(f'{self.name} поворачивает на {direction}!')

    def show_speed(self):
        print(f'{self.name}. Скорость: {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'{self.name}. Превышение скорости')


class WorkCar(Car):
    def show_speed(self):
        print(f'{self.name}. Скорость: {self.speed} км/ч')
        if self.speed > 40:
            print(f'{self.name}. Превышение скорости')


class PoliceCar(Car):
    pass


class SportCar(Car):
    pass

sport_car = SportCar(300, 'Красная', 'Спортивная машина', False)
town_car = TownCar(80, 'Черная', 'Городская машина', False)
work_car = WorkCar(60, 'Оранжевая', 'Рабочая машина', False)
police_car = PoliceCar(10, 'Голубая', 'Мусоровозка', True)

sport_car.show_speed()
sport_car.turn('лево')
town_car.go()
town_car.show_speed()
work_car.show_speed()
work_car.turn('право')
police_car.show_speed()
police_car.stop()

