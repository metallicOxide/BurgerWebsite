from backend.Ordering_system import OrderingSystem
from backend.Ingredient import Bun, Patty, MainsIngredient, Side, Drink
from backend.Order import Order
from backend.Inventory import Inventory
from backend.order_interface import DrinkOrder, SideOrder, MainOrder, Burger, Wrap
from backend.errors import OrderError
from backend.inventory_errors import AddStockError, UpdateQuantityError

import pytest

# Test File for Inventory Management

# Test add stock type

def test_add_bun():
    inventory = Inventory()
    inventory.add_stock_type('Sesame', "bun", 0.69, 10, 1, 4, "discrete")
    assert inventory.food_list[0].name == "Sesame bun"
    assert inventory.food_list[0].price  == 0.69
    assert inventory.food_list[0].max_allow == 4
    assert inventory.food_list[0].quant_type  == ""
    assert inventory.food_list[0].ingredient_size  == 1
    assert inventory.food_dict['Sesame bun'] == 10

def test_add_patty():
    inventory = Inventory()
    inventory.add_stock_type('yeet', "patty", 3, 15, 1, 3, "discrete")

    assert inventory.food_list[0].name == "yeet patty"
    assert inventory.food_list[0].price  == 3
    assert inventory.food_list[0].max_allow == 3
    assert inventory.food_list[0].quant_type  == ""
    assert inventory.food_list[0].ingredient_size  == 1
    assert inventory.food_dict['yeet patty'] == 15

def test_add_main_ingredient():
    inventory = Inventory()
    inventory.add_stock_type('tomato', "main", 0.2, 100000, 1, 20, "discrete")

    assert inventory.food_list[0].name == "tomato"
    assert inventory.food_list[0].price  == 0.2
    assert inventory.food_list[0].max_allow == 20
    assert inventory.food_list[0].quant_type  == "discrete"
    assert inventory.food_list[0].ingredient_size  == 1
    assert inventory.food_dict['tomato'] == 100000

def test_add_side_ingredient():
    inventory = Inventory()
    inventory.add_stock_type("Smoll fries", "side", 2.15, 10000, 75, 100000, "g")

    assert inventory.food_list[0].name == "Smoll fries"
    assert inventory.food_list[0].price  == 2.15
    assert inventory.food_list[0].max_allow == 100000
    assert inventory.food_list[0].quant_type  == "g"
    assert inventory.food_list[0].ingredient_size  == 75
    assert inventory.food_dict['Smoll fries'] == 10000


def test_add_drink_ingredient():
    inventory = Inventory()
    inventory.add_stock_type("Yogurt", "side", 2.56, 200000, 75, 300, "ml")

    assert inventory.food_list[0].name == "Yogurt"
    assert inventory.food_list[0].price  == 2.56
    assert inventory.food_list[0].max_allow == 300
    assert inventory.food_list[0].quant_type  == "ml"
    assert inventory.food_list[0].ingredient_size  == 75
    assert inventory.food_dict['Yogurt'] == 200000

def test_add_stock_exception_no_name():
    inventory = Inventory()

    with pytest.raises(AddStockError) as e:
        inventory.add_stock_type(None, "side", 2.56, 200000, 75, 300, "ml")
    assert str(e.value) == 'name'

def test_add_stock_exception_empty_name():
    inventory = Inventory()

    with pytest.raises(AddStockError) as e:
        inventory.add_stock_type("", "side", 2.56, 200000, 75, 300, "ml")
    assert str(e.value) == 'name'

def test_add_stock_exception_no_price():
    inventory = Inventory()

    with pytest.raises(AddStockError) as e:
        inventory.add_stock_type("Yogurt", "side", None, 200000, 75, 300, "ml")
    assert str(e.value) == 'price'

def test_add_stock_exception_empty_price():
    inventory = Inventory()

    with pytest.raises(AddStockError) as e:
        inventory.add_stock_type("Yogurt", "side", "", 200000, 75, 300, "ml")
    assert str(e.value) == 'price'

def test_add_stock_exception_negative_price():
    inventory = Inventory()

    with pytest.raises(AddStockError) as e:
        inventory.add_stock_type("Yogurt", "side", -5, 200000, 75, 300, "ml")
    assert str(e.value) == 'price'

def test_add_stock_exception_no_amount():
    inventory = Inventory()

    with pytest.raises(AddStockError) as e:
        inventory.add_stock_type("Yogurt", "side", 2, None, 75, 300, "ml")
    assert str(e.value) == 'amount'

def test_add_stock_exception_empty_amount():
    inventory = Inventory()

    with pytest.raises(AddStockError) as e:
        inventory.add_stock_type("Yogurt", "side", 2, "", 75, 300, "ml")
    assert str(e.value) == 'amount'

def test_add_stock_exception_negative_amount():
    inventory = Inventory()

    with pytest.raises(AddStockError) as e:
        inventory.add_stock_type("Yogurt", "side", 2, -200000, 75, 300, "ml")
    assert str(e.value) == 'amount'
    
def test_add_stock_exception_no_ing_size():
    inventory = Inventory()

    with pytest.raises(AddStockError) as e:
        inventory.add_stock_type("Yogurt", "side", 20, 200000, None, 300, "ml")
    assert str(e.value) == 'ingredient_size'

def test_add_stock_exception_empty_ing_size():
    inventory = Inventory()

    with pytest.raises(AddStockError) as e:
        inventory.add_stock_type("Yogurt", "side", 20, 200000, '', 300, "ml")
    assert str(e.value) == 'ingredient_size'

def test_add_stock_exception_negative_ing_size():
    inventory = Inventory()

    with pytest.raises(AddStockError) as e:
        inventory.add_stock_type("Yogurt", "side", 20, 200000, -75, 300, "ml")
    assert str(e.value) == 'ingredient_size'
    
def test_add_stock_exception_negative_max():
    inventory = Inventory()

    with pytest.raises(AddStockError) as e:
        inventory.add_stock_type("Yogurt", "side", 20, 200000, 75, -300, "ml")
    assert str(e.value) == 'max_allow'

def test_update_stock_quantity():
    inventory = Inventory()
    inventory.add_stock_type('Sesame', "bun", 0.69, 10, 1, 4, "discrete")
    assert inventory.food_list[0].name == "Sesame bun"
    assert inventory.food_list[0].price  == 0.69
    assert inventory.food_list[0].max_allow == 4
    assert inventory.food_list[0].quant_type  == ""
    assert inventory.food_list[0].ingredient_size  == 1
    assert inventory.food_dict['Sesame bun'] == 10

    inventory.update_stock_quantity('Sesame bun', 200)
    assert inventory.food_dict['Sesame bun'] == 210

def test_update_stock_quantity_exception_no_amount():
    inventory = Inventory()
    inventory.add_stock_type('Sesame', "bun", 0.69, 10, 1, 4, "discrete")
    assert inventory.food_list[0].name == "Sesame bun"
    assert inventory.food_list[0].price  == 0.69
    assert inventory.food_list[0].max_allow == 4
    assert inventory.food_list[0].quant_type  == ""
    assert inventory.food_list[0].ingredient_size  == 1
    assert inventory.food_dict['Sesame bun'] == 10

    with pytest.raises(UpdateQuantityError) as e:
        inventory.update_stock_quantity('Sesame bun', None)
    assert str(e.value) == 'Quantity cannot be empty'

def test_update_stock_quantity_exception_empty_amount():
    inventory = Inventory()
    inventory.add_stock_type('Sesame', "bun", 0.69, 10, 1, 4, "discrete")
    assert inventory.food_list[0].name == "Sesame bun"
    assert inventory.food_list[0].price  == 0.69
    assert inventory.food_list[0].max_allow == 4
    assert inventory.food_list[0].quant_type  == ""
    assert inventory.food_list[0].ingredient_size  == 1
    assert inventory.food_dict['Sesame bun'] == 10

    with pytest.raises(UpdateQuantityError) as e:
        inventory.update_stock_quantity('Sesame bun', "")
    assert str(e.value) == 'Quantity cannot be empty'

def test_update_stock_quantity_exception_negative_amount():
    inventory = Inventory()
    inventory.add_stock_type('Sesame', "bun", 0.69, 10, 1, 4, "discrete")
    assert inventory.food_list[0].name == "Sesame bun"
    assert inventory.food_list[0].price  == 0.69
    assert inventory.food_list[0].max_allow == 4
    assert inventory.food_list[0].quant_type  == ""
    assert inventory.food_list[0].ingredient_size  == 1
    assert inventory.food_dict['Sesame bun'] == 10

    with pytest.raises(UpdateQuantityError) as e:
        inventory.update_stock_quantity('Sesame bun', "abcdde")
    assert str(e.value) == 'Quantity must be an integer'




    

    
    
    
    

    