class Human:
    pass

class Student(Human):
    def __init__(self, name, age, grades=[]):
        self.name = name
        self.age = age
        self.grades = grades

    def __len__(self):
        return len(self.grades)

    def __str__(self):
        return f'{self.name}: {self.age}'

    def __add__(self, other):
        self.age += other
        return self.age

    def __lt__(self, other):
        return sum(self.grades)/len(self.grades) < sum(other.grades)/len(other.grades)

    def __getitem__(self, index):
        return self.grades[index]

    def __setitem__(self, index, value):
        self.grades[index] = value

    def __contains__(self, other):
        return other in self.grades

    def __iter__(self):
        self.iterations = 0
        return self

    def __next__(self):
        if self.iterations < len(self.grades):
            self.iterations += 1
            if self.grades[self.iterations - 1] % 2 == 0:
                return self.grades[self.iterations - 1]
        else:
            raise StopIteration

    # def __bool__(self):
    #     return False

    def num_grades(self):
        return len(self)

wasif = Student("Wasif", 28, [50, 60, 55])
anton = Student("Anton", 29, [95, 90, 90])
greg = Student("Greg", 27, [79, 82, 85, 90])
print(len(greg))
print(greg)
print(greg + 9)
print(greg > anton)
print(greg[2], greg[:2])
greg[2] = 67
print(greg.grades)
if greg:
    print(True)
print(6 in greg)
print(greg)
for i in greg:
    print(i)

