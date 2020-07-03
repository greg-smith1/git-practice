class Animal:
    pass

class Zoo:

    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

zoo = Zoo()
duck = Animal("duck")
zoo.add_animal(duck)
