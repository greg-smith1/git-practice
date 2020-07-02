class Worker:
    
    def __init__(self, name, job, years, department=None):
        self. name = name
        self.job = job
        self.years = years
        if department is None:
            self.department = ''
        else:
            self.department = department
        
    #@classmethod
    #def set_department(cls, department):
        #cls.departments.append(department)
        
    def increase_tenure(self, add_years=1):
        self.years += add_years
        
    def set_department(self, new_dept):
        if new_dept != self.department:
        self.department = new_dept
        
class Item:
    
    def __init__(self, name, explosive, weight, cost):
        self.name = name
        self.explosive = explosive
        self.weight = weight
        self.cost = cost
        
    def explode(self)
        if self.explode == True:
            print ('Boom!')
            
class Factory:
    days_since_last_incident =0
    def __init__(self, workers=None, products=None)
        if workers is None:
            self.workers = []
        else:
            self.workers = workers
        if products is None:
            self.products = []
        else:
            self.products = products
            
    
    def add_worker(self, workr):
        if workr not in self.workers:
            self.workers.append(workr)
            
    def create_product(self, item):
        if item not in self.products:
            self.products.append(item)
            
    def ship(self):
        self.products = []
            
    def add_day(self, day=1):
        self.days_since_last_incident += day
    
    def incident(self, reset=0):
        self.days_since_last_incident = reset
