from time import sleep
from itertools import cycle


class TrafficLight:

    def __init__(self):
        self.__colors = (('Red', 1), ('Yellow', 1), ('Green', 1))

    def running(self):
        for color, sec in cycle(self.__colors):
            print(color, f'(wait {sec} sec)')
            sleep(sec)


traffic_light = TrafficLight()
traffic_light.running()
