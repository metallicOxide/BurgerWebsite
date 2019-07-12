from abc import ABC
from backend.Inventory import Inventory

class OrderInterface(ABC):
    def __init__ (self):
        # dictionary with string name of item as key and
        # tells you quantity ie Dict{<name>,quantity}
        self._ingredients = {}

    def calc_suborder_price(self, inventory):
        total = 0.0
        for key in self.ingredients:
            # we need to use get_ingredient instead of key.price (key is a stirng)
            total += float(self.ingredients[key]) * float(inventory.get_ingredient(key).price)
        return round(total,2)

    def add_to_suborder(self, items):
        for key in items:
            if key in self.ingredients:
                self.ingredients[key] += items[key]
            else:
                # adding a new item into the order with quantity 1
                self.ingredients[key] = items[key]

    ''' Properties '''
    @property
    def ingredients(self):
        return self._ingredients

    def __str__(self):
        return '{0}'.format(self._ingredients)

''' Order subclasses '''
class DrinkOrder(OrderInterface):
    def __init__ (self):
        super().__init__()

class SideOrder(OrderInterface):
    def __init__ (self):
        super().__init__()

class MainOrder(OrderInterface):
    def __init__ (self):
        super().__init__()
        self._base_price = 0

    # is it possible to not repeat this function by setting base_price above?
    def calc_suborder_price(self, inventory):
        total = self._base_price
        for key in self._ingredients:
            total += self._ingredients[key] * inventory.get_ingredient(key).price
        return total

    @property
    def base_price(self):
        return self._base_price

class Burger(MainOrder):
    def __init__ (self):
        super().__init__()
        self._base_price = 3

class Wrap(MainOrder):
    def __init__ (self):
        super().__init__()
        self._base_price = 3.5
