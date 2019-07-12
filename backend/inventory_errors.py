class AddStockError(Exception):
    def __init__(self, errors, msg=None):
        if msg is None:
            msg = "%s"%(', '.join(errors.keys()))

        super().__init__(msg)

        self.errors = errors

class UpdateQuantityError(Exception):
    def __init__(self, error, msg=None):
        if msg is None:
            msg = "%s" % error

        super().__init__(msg)

        self.error = error

def check_add_stock_error(name, classification, price, amount, max_allow, ingredient_size):
    errors = {}
    if name == None or name == "":
        errors["name"] = "Name cannot be empty"
    if classification == "":
        errors["classification"] = "Please select a classification"
    if price == None or price == "":
        errors["price"] = "Price cannot be empty"
    elif price < 0:
        errors["price"] = "Price must be positive"
    if amount == None or amount == "":
        errors["amount"] = "Quantity cannot be empty"
    elif amount <= 0:
        errors["amount"] = "Quantity must be positive"
    if max_allow != float("inf") and max_allow <= 0:
        errors["max_allow"] = "Max allowed must be positive"
    if ingredient_size == None or ingredient_size == '':
        errors["ingredient_size"] = "Ingredient size cannot be empty"
    elif ingredient_size <= 0:
        errors["ingredient_size"] = "Ingredient size must be positive"
    return errors

def check_update_quantity_error(amount):
    error = ""
    if amount == "" or amount == None:
        error = "Quantity cannot be empty"
    else:
        try:
            int(amount)
        except ValueError:
            error = "Quantity must be an integer"
    return error
