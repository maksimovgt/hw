class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_mass_test(self):
        return (self._length * self._width * 25 * 5) / 1000


road = Road(5000, 20)
print(road.get_mass_test())
