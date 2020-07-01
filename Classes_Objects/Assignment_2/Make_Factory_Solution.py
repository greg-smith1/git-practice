class Worker:
    def __init__(self, name, job, years, department=None):
        self.name=name
        self.job=job
        self.years=years
        self.department=department

    def set_department(self, new_dept):
        self.department=new_dept

    def increase_tenure(self):
        self.years+=1

# testing above code
bob=Worker("bob", "builder", 0)
# bob.set_department("construction")
# bob.increase_tenure()
# print(bob.department)
# print(bob.years)

class Item:
    def __init__(self, name, explosive, weight, cost):
        self.name=name
        self.explosive=explosive
        self.weight=weight
        self.cost=cost

    def explode(self):
        if self.explosive:
            print("Boom!")

# testing above code
fork=Item("fork", False, 4, 1.0)
# fork.explode()
# print(fork.cost)
spork=Item("spork", True, 3, 5.0)
# spork.explode()

class Factory:
    def __init__(self, workers, products=[], days_since_last_incident=0):
        self.workers=workers
        self.products=products
        self.days_since_last_incident=days_since_last_incident

    def add_worker(self, Worker):
        self.workers.append(Worker)
    
    def create_product(self, Item):
        self.products.append(Item)
    
    def ship(self):
        self.products=[]

    def add_day(self):
        self.days_since_last_incident+=1

    def incident(self):
        self.days_since_last_incident=0

acme=Factory([])
acme.add_worker(bob)
acme.create_product(fork)
print(acme.workers)
print(acme.products)
acme.ship()
print(acme.products)
acme.add_day()
print(acme.days_since_last_incident)
acme.incident()
print(acme.days_since_last_incident)

