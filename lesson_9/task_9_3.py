from decimal import Decimal


class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income['wage']
        self._income_bonus = income['bonus']


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname} {self.position}'

    def get_total_income(self):
        return Decimal(self._income_wage + self._income_bonus).quantize(Decimal('1.00'))


pos = Position('Pavel', 'Grosberg', 'Chief Specialist in Cost Estimation', {'wage': 115_972.12, 'bonus': 34_694.54})
print(pos.get_full_name())
print(pos.get_total_income())
