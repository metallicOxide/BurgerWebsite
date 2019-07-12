from backend.Ingredient import Bun, Patty, MainsIngredient, Side, Drink
from backend.Order import Order
from backend.Inventory import Inventory
from backend.order_interface import DrinkOrder, SideOrder, MainOrder, Burger, Wrap

class OrderError(Exception):
    def __init__(self, errors, msg=None):
        string = ''
        if msg is None:
            for key in errors:
                string += key + ".\n"
            msg = string
        super().__init__(msg)

        self.errors = errors

class TrackOrderError(Exception):
    def __init__(self, errors, msg=None):
        string = ''
        if msg is None:
            for key in errors:
                string += key + ".\n"
            msg = string
        super().__init__(msg)


        self.errors = errors

class StatusError(Exception):
    def __init__(self, errors, msg=None):
        string = ''
        if msg is None:
            for key in errors:
                string += key + ".\n"
            msg = string
        super().__init__(msg)


        self.errors = errors

class ClearOrderError(Exception):
    def __init__(self, errors, msg=None):
        string = ''
        if msg is None:
            for key in errors:
                string += key + ".\n"
            msg = string
        super().__init__(msg)


        self.errors = errors

def check_checkout_error(system, mains, sides, drinks, inventory):
    errors = {}
    if ((mains == "" or mains == None or mains == []) and (sides == "" or sides == None or sides == {}) and (drinks == None or drinks == "" or drinks == {})):
        errors["Invalid order, please add in a main/side/drink"] = "invalid order"
    if inventory == "" or inventory == None:
        errors["Invalid Inventory specified"] = "Inventory error"
    return errors



def check_order_error(system, ID, items, inventory):
    errors = {}

    if ID != "temp":
        curr_ID = None
        for order in system._curr_orders:
            if order.ID == ID:
                curr_ID = ID
                break
        completed_ID = None
        for order in system._completed_orders:
            if order.ID == ID:
                completed_ID = ID
                break
        if system == "" or system is None:
            errors["Please enter a valid order system"] = "no order"    

        # ID validity check  
        if curr_ID == None and completed_ID == None:
            errors["ID: {0} does not exist, please specify a valid ID".format(ID)] = "The ID user specified does not exist" 

    if inventory == "" or inventory is None:
        errors["Please enter a valid inventory system"] = "no inventory"
    # check for valid item input
    if items == "" or items is None:
        errors["Please enter add a side or ingredient to the order"] = "no item added"

    # Inventory/Order Checking
    num_bun = 0
    num_patty = 0
    max_bun = 0
    min_bun = 0
    max_patty = 0
    for key in items:
        # count number of bun and number of patty
        ingredient = inventory.get_ingredient(key)

        if ingredient == None:
            errors["We do not serve '{0}', please specify a valid item".format(key)] = "Item not in inventory"
        # ingredient stock validity check
        else:
            if ingredient.classification == 'bun':
                max_bun = ingredient.max_allow
                min_bun = ingredient.min_allow 
                num_bun += items[key]
            if ingredient.classification == 'patty':
                max_patty = ingredient.max_allow
                num_patty += items[key]

            if int(inventory.get_stock_quantity(key)) < items[key]:
                errors["Order exceeds inventory: Only {0} of {1} left in inventory".format(inventory.get_stock_quantity(key), key)] = "item out of stock"
            # Max amount validity check
            if items[key] > ingredient.max_allow and ingredient.classification != ('patty' or 'bun'):
                errors["Maximum allowable limit for {0} is {1}".format(ingredient.name, ingredient.max_allow)] = "User ordering more than maximum allowed limit"
    # max/min amount validity check
    if num_patty > max_patty:
        errors["Maximum ordering limit for patty is {0}".format(max_patty)] = "User ordering more than patty limit"
    if num_bun > max_bun:
        errors["Maximum ordering limit for bun is {0}".format(max_bun)] = "User ordering more than max bun limit"
    elif num_bun < min_bun:
        errors["Minimum ordering limit for bun is {0}".format(min_bun)] = "User ordering less than min bun limit"     

    return errors


def check_order_status_error(system, Status, List, ID):
    errors = {}
    if List == "" or List is None:
        errors["Please specify if the order is current or completed"] = "Specify a either curr_order or completed_orders"
    if Status != None:
        if Status != "Preparing" and Status != "Ready for collection" and Status != "Collected":
            errors["Please provide an Order Status from the drop down list"] =\
            "Order Status can only be preparing, ready for collection or collected"
    i = False
    for order in system._curr_orders:
        if ID == order.ID:
            i = True
            break
    if i == False:
        for order in system._completed_orders:
            if ID == order.ID:
                i = True
                break
    if i == False:
        errors["ID does not exist. Please specify a valid ID"] = "The ID user specified does not exist"
    return errors

def check_clear_order_error(system, List, ID=None):
    errors = {}
    if List == "" or List is None:
        errors["Please specify if the order is current or completed"] = "Specify a either curr_order or completed_orders"

    if ID != None:
        i = False
        for order in system._curr_orders:
            if ID == order.ID:
                i = True
                break
        if i == False:
            for order in system._completed_orders:
                if ID == order.ID:
                    i = True
                    break
        if i == False:
            errors["ID does not exist. Please specify a valid ID"] = "The ID user specified does not exist"

    return errors

def check_id_error(system, ID):
    errors = {}
    if ID == '' or ID == None:
        errors['Invalid ID'] = "ID does not exsist. Please enter a valid ID"
    elif ID != '' or ID != None:
        found = False
        for order in system.curr_orders:
            if ID == order.ID:
                found = True
                break
        if found == False:
            errors['Invalid ID'] = "ID does not exsist. Please enter a valid ID"
    return errors


def check_comp_order_id_error(system, ID):
    errors = {}
    if ID == '' or ID == None:
        errors['Invalid ID'] = "ID does not exsist. Please enter a valid ID"
    elif ID != '' or ID != None:
        found = False
        for order in system.completed_orders:
            if ID == order.ID:
                found = True
                break
        if found == False:
            errors['Invalid ID'] = "ID does not exsist. Please enter a valid ID"
    return errors
