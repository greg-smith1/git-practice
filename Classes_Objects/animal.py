class Animal:    
    def __init__(self, name, species=None, noise=None):
        self.name = name
        self.species = species
        self.noise = noise
        
    def make_noise(self, noise=None):
        return self.noise

class Tiger(Animal):
    def __init__(self, name, species='tiger', noise='Roar!'):
        Animal.__init__(self, name, species, noise)
        
class Dog(Animal):
    def __init__(self, name, species='dog', noise="Bark!"):
        Animal.__init__(self, name, species, noise)
        
class Cow(Animal):
    def __init__(self, name, species='cow', noise='Moo!'):
        Animal.__init__(self, name, species, noise)
        

class Zoo:
    def __init__(self, animals=None):
        if animals is None:
            self.animals = []
        else:
            self.animals = animals
        
    def add(self, ani):
        if ani not in self.animals:
            self.animals.append(ani)
              
    def show_animals(self):
        for i in self.animals:
            print(f'{self.name} is a {self.species}. Noise:{self.make_noise(i)}')

tony = Tiger('Tony')
print(tony.species)
print(tony.make_noise())

mike = Tiger("Mike")
molly = Dog("Molly")
bessie = Cow("Bessie")

zoo = Zoo()
zoo.add(mike)
zoo.add(molly)
zoo.add(bessie)
print(zoo.animals)

zoo.show_animals()