# Создаем базовый класс
class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f'{self.name} принимает пищу (любит покушать :)') #продемонстрируем полиморфизм через принт

# Наследование: создаем классы птиц, млекопитающих и рептилий
class Bird(Animal):
    def make_sound(self):
        print(f'{self.name} поет свою птичью песню')

class Mammal(Animal):
    def make_sound(self):
        print(f'{self.name} рычит, ревет, шумит')

class Reptile(Animal):
    def make_sound(self):
        print(f'{self.name} шипит')

# Функция для демонстрации полиморфизма
def animal_sounds(animals):
    for animal in animals:
        animal.make_sound()

# Композиция: создаем Зоопарк с животными и служащими
class Zoo():
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} добавлен в группу животных зоопарка")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"{employee.name} добавлен в сотрудники зоопарка")

# Специфические методы для сотрудников
class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feeds_animal(self, animal):
        print(f"{self.name} кормит {animal.name}")

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heals_animal(self, animal):
        print(f"{self.name} лечит {animal.name}")

# Создаем экземпляры классов животных
animals = [
    Bird("Ворон Егор", 150),
Mammal("Гепард Гавриил", 8),
Reptile("Варан Вартан", 15),
Mammal("Слон Гоша", 5)
]

# Создаем экземпляры классов сотрудников
zookeeper = ZooKeeper("Роман Сергеевич")
veterinarian = Veterinarian("Денис Владимирович")

# Создаем зоопарк и добавляем животных и сотрудников
zoo = Zoo()
for animal in animals:
    zoo.add_animal(animal)

zoo.add_employee(zookeeper)
zoo.add_employee(veterinarian)

# Продемонстрируем полиморфизм
animal_sounds(animals)

animals[1].eat()

ZooKeeper.feeds_animal(zookeeper, animals[1])

Veterinarian.heals_animal(veterinarian, animals[2])
