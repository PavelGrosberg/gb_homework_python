from abc import ABC, abstractmethod
from random import choice


class WareHouse:
    __storage = []

    def put(self, device):
        if not isinstance(device, OfficeEquipment):
            raise ValueError('Only OfficeEquipment supported')
        self.__storage.append(device)

    def get(self, count=None, **kwargs):
        if count is not None:
            if not type(count) is int:
                raise TypeError('Unsupported type for count')
            if count < 1:
                raise ValueError('Unsupported value for count')

        if not set(kwargs.keys()).issubset(OfficeEquipment.approved_keys):
            raise KeyError(f'Unsupported filter request {list(kwargs.keys())}.'

                           f' Should be part of {OfficeEquipment.approved_keys}')

        res_list = []
        for el in self.__storage:
            for k, v in kwargs.items():
                if getattr(el, k) != v:
                    break
            else:
                res_list.append(el)
                if count:
                    count -= 1
                    if not count:
                        break
        if count:
            raise Exception('Not enough elements')

        for el in res_list:
            self.__storage.remove(el)
        return res_list

    def __repr__(self):
        return str(self.__storage)

    def __len__(self):
        return len(self.__storage)

    def get_report(self):
        pres = {}
        for el in self.__storage:
            ce = pres.get(el.device_type) or 0
            ce += 1
            pres[el.device_type] = ce
        return "WareHouse have {}".format(str(pres).strip('{}'))


class OfficeEquipment(ABC):
    serial_number: int
    model: str
    manufacturer: str
    cost: int
    department = ''
    approved_keys = ('serial_number', 'model', 'manufacturer', 'department', 'device_type', 'cost')

    def __init__(self, manufacturer, model, serial_number, cost=0):
        self.manufacturer = manufacturer
        self.model = model
        if not type(serial_number) is int:
            raise ValueError('Unsupported type for serial number')
        self.serial_number = serial_number
        if not type(cost) is int:
            raise ValueError('Unsupported type for cost')

        self.cost = cost

    def __repr__(self):
        return f'"{self.device_type}: {self.manufacturer} {self.model} SN: {self.serial_number}"'

    @property
    @abstractmethod
    def device_type(self):
        pass


class Printer(OfficeEquipment):
    __serial = 0

    def __init__(self, manufacturer, model, speed, cost=0):
        Printer.__serial += 1
        super().__init__(manufacturer, model, Printer.__serial, cost)
        self.speed = speed

    @property
    def device_type(self):
        return 'Printer'


class Scanner(OfficeEquipment):
    __serial = 0

    def __init__(self, manufacturer, model, size='A4', resolution=300, cost=0):
        Scanner.__serial += 1
        super().__init__(manufacturer, model, Scanner.__serial, cost)
        self.size = size
        self.resolution = resolution

    @property
    def device_type(self):
        return 'Scanner'


class Copier(OfficeEquipment):
    __serial = 0

    def __init__(self, manufacturer, model, speed=120, size='A5', resolution=300, cost=0):
        Copier.__serial += 1
        super().__init__(manufacturer, model, Copier.__serial, cost)

        self.speed = speed
        self.size = size
        self.resolution = resolution

    @property
    def device_type(self):
        return 'Xerox'


wh = WareHouse()
p = Printer('Samsung', 'ml100', 120, 1200)
p2 = Printer('Brother', 'br100', 120, 1000)
s1 = Scanner('Hp', 'iScan', 'A4', 300, 500)
s2 = Scanner('Brother', 'Superscan', 'A5', 600, 1500)
c1 = Copier('Brother', 'SuperCopy', 100, 'A5', 600, 2500)
c2 = Copier('HP', 'Fake', 100, 'A5', 600, 2500)
print(c2)

wh.put(p)
wh.put(p2)
wh.put(s1)
for x in [Scanner('Brother', '', cost=1000 + i * 10) for i in range(45)]:
    x.model = choice(('Superscan', 'Superscan2', 'ScanMe', 'ScanMaster'))
    x.department = choice(('HR', 'DEV', 'QA', 'Marketing'))
    wh.put(x)
print(len(wh))
print(wh.get_report())
l1 = wh.get(device_type='Scanner', model='Superscan', department='DEV')
print('l1', len(l1), l1)
l2 = wh.get(device_type='Printer', cost=1200)
print('l2', len(l2))
l4 = wh.get(cost=1200)
print('l4', len(l4), l4)
print('wh', len(wh))
#
try:
    l3 = wh.get(35)
except Exception as err:
    print(err)
else:
    print(len(l3), l3)
print('wh', len(wh))
