class Animal():
     def __init__(self, name, age):
         self.name = name
         self.age = age


     def eat(Self):
         print("кушает")
     def male_sound(self):
         pass

class Bird(Animal):
    def make_sound(self):
        print('чирик чирик')


class Mammal(Animal):
    def make_sound(self):
        print("гав")

class Reptile(Animal):
     def make_sound(self):
        print('шсшсшсшсшс')

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()
class Zoo():
    def __init__(self):
        self.animals = []
        self.staff = []
    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлеено в зоопарк")

    def add_staff(self, new_staff):
        self.staff.append(new_staff)
        print(f"сотрудник {new_staff} добавлеено в зоопарк")
class ZooKeeper():
    def feed_animal(self, animal):
        print(f"Сотрудник кормит {animal.name}")

class Veterinarian():
    def feed_animal(self, animal):
        print(f"ветеринар лечит {animal.name}")


bird1 = Bird("Птица","1")
mammal1 = Mammal("Собака", "2")
reptile1 = Reptile("Ящерица","3")

zoo = Zoo()
keeper = ZooKeeper()
veterinarian = Veterinarian()

zoo.add_animal(bird1)
zoo.add_animal(mammal1)
zoo.add_animal(reptile1)

