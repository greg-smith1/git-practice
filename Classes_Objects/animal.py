class Animal:    
    def __init__(self, name, species=None, noise=None):
        self.name = name
        self.species = species
        self.noise = noise
        
    def __str__(self):
        if self.name:
            return f"<{self.name}>"
        else:
            return "<>"
        
    def make_noise(self):
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
        

class Zoo():
    def __init__(self):
        self.animals = []
        
    def add(self, ani):
        if ani not in self.animals:
            #self.animals.append((ani))
            self.animals.append((ani.name, ani.species, ani.noise))
                         
    def show_animals(self):
        for i in self.animals:
            print(f'{i[0]} is a {i[1]}.')
            print(i[2])

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
print(zoo.animals[:])
print(molly)

zoo.show_animals()