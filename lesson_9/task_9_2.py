class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass(self):
        weight = int(self._length * self._width * 25 * 5 / 1000)
        return weight


myRoad = Road(20, 5000)
print(myRoad.calc_mass(), 'т')