
class Item:

    categories = []

    def __init__(self, name, brand, price, inventory, category, item_id=None):
        self.name = name
        self.brand = brand
        self.price = price
        self.inventory = inventory
        self.category = category
        self.item_id = item_id
    
    def update_inventory(self, quantity=-1):
        # Either sell or re-stock an item, with negative values representing sales
        # and positive representing re-stocking an item
        self.inventory += quantity

    @classmethod
    def add_category(cls, category):
        cls.categories.append(category)

pants = Item("pants", "levis", 20.99, 7, "clothing")
print(pants.item_id)
pants.update_inventory()
print(pants.inventory)
pants.update_inventory(90)
print(pants.inventory)
