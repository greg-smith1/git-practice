class Animal:
    def __init__(self, name, species=None):
        self.name=name
        self.species=species

    def make_noise(self):
        print("")

class Tiger(Animal):
    def __init__(self, name, species="tiger"):
        Animal.__init__(self,name, species)
    def make_noise(self):
        print("Roar!")

class Dog(Animal):
    def __init__(self, name, species="dog"):
        Animal.__init__(self,name, species)
    def make_noise(self):
        print("Bark!")
class Cow(Animal):
    def __init__(self, name, species="cow"):
        Animal.__init__(self,name, species)
    def make_noise(self):
        print("Moo!")

class Zoo:
    animals=[]
    @classmethod
    def add(cls,animal):
        if isinstance(animal, Animal):
            cls.animals.append(animal)
        else:
            raise TypeError

    @classmethod
    def show_animals(cls):
        for i in cls.animals:
            print(i.name+" the "+i.species)
            i.make_noise()

# testing the code above
mike = Tiger("Mike")
molly = Dog("Molly")
bessie = Cow("Bessie")
zoo = Zoo()
zoo.add(mike)
zoo.add(molly)
zoo.add(bessie)
zoo.show_animals()
print(mike.species)


