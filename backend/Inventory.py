from backend.Ingredient import Bun, Patty, MainsIngredient, Side, Drink
from backend.inventory_errors import *

class Inventory():
    def __init__(self):
        self._food_dict = {}
        self._food_list = []

    @property
    def food_list(self):
        return self._food_list

    @property
    def food_dict(self):
        return self._food_dict

    def browse_menu(self):
        buns = []
        patties = []
        wraps = []
        misc = []
        sides = []
        drinks = []
        for food in self.food_list:
            if food.classification == 'bun':
                buns.append(food)
            if food.classification == 'patty':
                patties.append(food)
            if 'wrap' in food.name.lower():
                wraps.append(food)
            if food.classification == 'main' and food.name.lower() != 'wrap':
                misc.append(food)
            if food.classification == 'side':
                sides.append(food)
            if food.classification == 'drink':
                drinks.append(food)

        print("\n\nViewing menu: \n\nMains: \n")
        print("Buns: \n")
        for item in buns:
            print(item.name + ", price: " + str(item.price) + ", max allowed: " + str(item.max_allow))
        print("\n")
        print("Wraps: \n")
        for item in wraps:
            print(item.name + ", price: " + str(item.price))
        print("\n")
        print("Patties: \n")
        for item in patties:
            print(item.name + ", price: " + str(item.price) + ", max allowed: " + str(item.max_allow))
        print("\n")
        print("Other ingredients: \n")
        for item in misc:
           print(item.name + ", price: " + str(item.price))
        print("\n")
        print("Sides: \n")
        for item in sides:
            print(item.name + ", price: " + str(item.price))
        print("\n")
        print("Drinks: \n")
        for item in drinks:
            print(item.name + ", price: " + str(item.price))

    def get_ingredient(self, name):
        for key in self._food_list:
            if key.name.lower() == name.lower():
                return key
        return None

    def update_stock_quantity(self, name, amount):
        try:
            error = check_update_quantity_error(amount)
            if error:
                raise UpdateQuantityError(error)
        except UpdateQuantityError as e:
            raise e
        else:
            self._food_dict[name] = self._food_dict[name] + amount

    def add_stock_type(self, name, classification, price, amount, ingredient_size = None, max_allow = None, quant_type = None):
        errors = {}
        try:
            errors = check_add_stock_error(name, classification, price, amount, max_allow, ingredient_size)
            if errors:
                raise AddStockError(errors)
        except AddStockError as e:
            print(e)
            raise e
        else:
            if classification.lower() == 'bun':
                food = Bun(name, price, ingredient_size)
            elif classification.lower() == 'patty':
                food = Patty(name, price, ingredient_size)
            elif classification.lower() == 'main':
                food = MainsIngredient(name, price, max_allow, quant_type, ingredient_size)
            elif classification.lower() == 'side':
                food = Side(name, price, max_allow, quant_type, ingredient_size)
            elif classification.lower() == 'drink':
                food = Drink(name, price, max_allow, quant_type, ingredient_size)

            self._food_list.append(food)
            self._food_dict[food.name] = amount

    def get_stock_quantity(self, name):
        for key in self._food_list:
            if key.name.lower() == name.lower():
                return self._food_dict[key.name]
        return None

    def delete_stock(self, name):
        self._food_dict.pop(name)
        for key in self._food_list:
            if key.name.lower() == name.lower():
                index = self._food_list.index(key)
                self._food_list.pop(index)

            
