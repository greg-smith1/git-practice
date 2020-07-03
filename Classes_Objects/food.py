class Food:
    def __init__(self, name, healthy, price):
        self.name = name
        self.healthy = healthy
        self.price = price
        
class ShoppingList:
    def __init__(self, shopping_list=None):
        if shopping_list is None:
            self.shopping_list = []
        else:
            self.shopping_list = shopping_list
            
    def add(self, item):
        if item not in self.shopping_list:
            self.shopping_list.append((item.name, item.healthy, item.price))

    def view(self):
        total = 0
        for i in self.shopping_list:
            total += i[2]
            print(f'One {i[0]} costs {i[2]}. Total cost is {total}.')
        
apple = Food('apple', True, 0.75) 
candy = Food('candy', False, 0.50)

shoppinglist = ShoppingList()
shoppinglist.add(apple)
shoppinglist.add(candy)

shoppinglist.view()