from backend.Ingredient import Bun, Patty, MainsIngredient, Side, Drink
from backend.Order import Order
from backend.Inventory import Inventory
from backend.errors import *

class OrderingSystem():
    def __init__(self):
        self._curr_orders = []
        self._completed_orders = []

    @property
    def curr_orders(self):
        return self._curr_orders

    @property
    def completed_orders(self):
        return self._completed_orders

    @property
    def deleted_orders(self):
        return self._deleted_orders

    def get_curr_order_by_ID(self, ID):
        errors = {}
        try:
            errors = check_id_error(self, ID)
            if errors:
                raise TrackOrderError(errors)
        except TrackOrderError as error:
            print(error)
            raise error
            return None
        else:
            for order in self.curr_orders:
                if order.ID == ID:
                    return order
        return None

    def get_completed_order_by_ID(self, ID):
        errors = {}
        try:
            errors = check_comp_order_id_error(self, ID)
            if errors:
                raise TrackOrderError(errors)
        except TrackOrderError as error:
            print(error)
            raise error
            return None
        else:
            for order in self.completed_orders:
                if order.ID == ID:
                    return order
        return None

    # keyword search <- this should be inventory
    # User Story 1.2 does not need to be implemented in the current iteration
    def keyword_ingredient_search(self, name, classification, inventory):
        result = []
        found = 0
        for ingredient in inventory.food_list:
            ing_classification = ingredient.classification.lower()
            if ing_classification == 'bun' or ing_classification == 'patty':
                ing_classification = 'main'
            # find function returns -1 if not in string
            if ingredient.name.lower().find(name.lower()) != -1 and ing_classification == classification.lower():
                result.append(ingredient)
                found += 1
        if found == 0:
            return "No results found, Please try again"

        return result

    # passes in main, side, drink objects to create order object
    # push order into current order and returns order
    def create_order(self, ID):
        new = Order(ID)
        self._curr_orders.append(new)
        return new


    # classification: where to add it to
    def add_to_order(self, ID, items, inventory):
        # items-> a list of food
        errors = {}
        try:
            errors = check_order_error(self, ID, items, inventory)
            if errors:
                raise OrderError(errors)
        except OrderError as error:
            # raise to higher level
            print(error)
            raise error
        else:
            if len(items) == 0:
                return None
            order = self.get_curr_order_by_ID(ID)
            classification = inventory.get_ingredient(list(items.keys())[0]).classification.lower()
            if classification == "drink":
                order.add_drink(items)
            if classification == "side":
                order.add_side(items)
            if classification == "main" or classification == "bun" or classification == "patty":
                order.add_main(items, inventory)
        return None

    def create_ID(self):
        ID = 0
        for order in self._curr_orders:
            if order.ID >= ID:
                ID = order.ID + 1
        for order in self._completed_orders:
            if order.ID >= ID:
                ID = order.ID + 1
        return ID

    def check_ingredient_max(self, item, inventory):
        return inventory.get_ingredient(item).max_allow

    def checkout(self, mains, sides, drinks, inventory):
        errors ={}
        try:
            errors = check_checkout_error(self, mains, sides, drinks, inventory)
            if errors:
                raise OrderError(errors)
        except OrderError as error:
            # generate id
            print(error)
            raise error
        else:
            ID = self.create_ID()
            # for order in self._curr_orders:
            #     if order.ID == ID:
            #         ID = order.ID + 1
            # for order in self._completed_orders:
            #     if order.ID == ID:
            #         ID = order.ID + 1
            # creates order and adds mains, sides and drinks in
            self.create_order(ID)

            if mains != None and mains != "":
                for item in mains:
                    self.add_to_order(ID, item, inventory)
            if sides != None and sides != "":
                self.add_to_order(ID, sides, inventory)
            if drinks != None and drinks != "":
                self.add_to_order(ID, drinks, inventory)

            self.update_inventory(mains, sides, drinks, inventory)

        return ID

    def update_inventory(self, mains, sides, drinks, inventory):
        if mains != None and mains !='': 
            for main in mains:
                for item in main:
                    ingredient = inventory.get_ingredient(item)
                    inventory.update_stock_quantity(item, -(main[item]*ingredient.ingredient_size))
        if sides !=  None and sides !='':  
            for item in sides:
                ingredient = inventory.get_ingredient(item)
                inventory.update_stock_quantity(item, -(sides[item]*ingredient.ingredient_size))
        if drinks != None and drinks != '':
            for item in drinks:
                ingredient = inventory.get_ingredient(item)
                inventory.update_stock_quantity(item, -(drinks[item]*ingredient.ingredient_size))
        return None

    def staff_view_orders(self, inventory):
        for order in self.curr_orders:
            order.print_order(inventory)

    def staff_view_completed_orders(self, inventory):
        for order in self.completed_orders:
            order.print_order(inventory)

    # check status of orders for each order in the curr order list. If the
    # status of the order is completed, move the order to the completed list
    # and remove the order from curr_orders list

    def set_order_status(self, Status, ListString, ID):
        errors = {}
        try:
            errors = check_order_status_error(self, Status, ListString, ID)
            if errors:
                raise StatusError(errors)
        except StatusError as error:
            print(error)
            raise error
        else:
            if ListString == "Current":
                order = self.get_curr_order_by_ID(ID)
                order.update_status(Status)
                if Status == "Collected":
                    self.completed_orders.append(order)
                    self.curr_orders.remove(order)
            elif ListString == "Completed":
                order = self.get_completed_order_by_ID(ID)
                order.update_status(Status)
                if Status != "Collected":
                    self.curr_orders.append(order)
                    self.completed_orders.remove(order)
            elif ListString == "Deleted":
                order = self.get_deleted_order_by_ID(ID)
                order.update_status(Status)
                if Status == "Collected":
                    self.completed_orders.append(order)
                    self.deleted_orders.remove(order)
                elif Status != "Collected":
                    self.curr_orders.append(order)
                    self.deleted_orders.remove(order)

        return None

    
    def clear_orders(self, List, ID=None):
        errors = {}
        try:
            errors = check_clear_order_error(self, List, ID)
            if errors:
                raise ClearOrderError(errors)
        except ClearOrderError as error:
            print(error)
            raise error
        else:
            if List == "Current" and ID == None:
                self._curr_orders.clear()
            elif List == "Completed" and ID == None:
                self._completed_orders.clear()
            elif List == "Current" and ID != None:
                for order in self._curr_orders:
                    if ID == order._orderID:
                        self._curr_orders.remove(order)
            elif List == "Completed" and ID != None:
                for order in self._completed_orders:
                    if ID == order._orderID:
                        self._completed_orders.remove(order)
        return None
