from backend.order_interface import DrinkOrder, SideOrder, Burger, Wrap
from backend.Ingredient import Bun, Patty, MainsIngredient, Side, Drink
from backend.Inventory import Inventory

class Order():
    # will pass in mains order, drink order and sides order
    def __init__(self, orderID):
        self._orderID = orderID
        self._status = "Preparing"
        self._price = 0
        self._mains = []
        self._drinks = DrinkOrder()
        self._sides = SideOrder()

    @property
    def ID(self):
        return self._orderID

    @property
    def status(self):
        return self._status

    # setter
    def update_status(self, status):
        self._status = status

    @property
    def mains(self):
        return self._mains

    @property
    def sides(self):
        return self._sides

    @property
    def drinks(self):
        return self._drinks

    @property
    def price(self):
        return self._price

    def calculate_order_price(self, inventory):
        price = 0
        # we assume mains is a list of main subclasses
        for main in self.mains:
            price += main.calc_suborder_price(inventory)
        price += self.drinks.calc_suborder_price(inventory)
        price += self.sides.calc_suborder_price(inventory)
        return round(price,2)

    # added make_main, make_drink and make_side
    # creates main and pushes that shit into main_order_array
    # (need array to deal with multiple mains in 1 order)
    def add_main(self, items, inventory):
        Isburger = 0
        for key in items:
            food = inventory.get_ingredient(key)
            if isinstance(food, Bun):
                Isburger = 1
                break

        if Isburger:
            main = Burger()
        else:
            main = Wrap()

        main.add_to_suborder(items)
        self._mains.append(main)

    def add_drink(self, items):
        self._drinks.add_to_suborder(items)

    def add_side(self, items):
        self._sides.add_to_suborder(items)

    def print_order(self, inventory):
        output = 'OrderID: {0}\n'.format(self._orderID)
        output += 'Mains: '
        for main in self._mains:
            output += '{0} '.format(main)
        output += '\nSides: {0}\n'.format(self._sides)
        output += 'Drinks: {0}\n'.format(self._drinks)
        output += 'Price: {0}\n'.format(self.calculate_order_price(inventory))
        output += 'Status: {0}\n'.format(self._status)
        print(output)
        return output
