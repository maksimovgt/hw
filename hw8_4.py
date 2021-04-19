class Store:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель': self.name, 'Цена': self.price, 'Кол-во': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} кол-во {self.quantity}'

    def reception(self):
        try:
            unit = input(f'Введите модель ')
            unit_1 = int(input(f'Введите цену '))
            unit_2 = int(input(f'Введите кол-во '))
            unique = {'Модель устройства': unit, 'Цена за ед': unit_1, 'Количество': unit_2}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Список: -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'************')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return Store.reception(self)


class Printer(Store):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(Store):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Copier(Store):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'


unit_1 = Printer('hp', 2000, 5, 10)
unit_2 = Scanner('Canon', 1200, 5, 10)
unit_3 = Copier('Xerox', 1500, 1, 15)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())