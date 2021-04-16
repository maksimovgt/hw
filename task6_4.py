class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.speed = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернулась {direction}')

    def show_speed(self):
        print(f'скорость {self.name}: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        print(f'{self.name} скорость: {self.speed} Скорость превышена!' if self.speed > 60 else f'{self.name}: Скорость автомобиля - {self.speed}')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'{self.name} скорость: {self.speed} - ПРЕВЫШЕНИЕ СКОРОСТИ!!!' \
                  if self.speed > 40 else f'{self.name}: Скорость автомобиля - {self.speed}')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


police = PoliceCar(100, 'сине-белый', 'ДПС', True)
ferrari = SportCar(200, 'желтый', 'Феррари', False)
cargo = WorkCar(50, 'черный', 'Фургон', False)
prius = TownCar(50, 'белый', 'Приус', False)


police.stop()
cargo.go()
prius.turn('налево')
ferrari.turn('направо')
print(f'')
print('-' * 100)
print(cargo.show_speed())