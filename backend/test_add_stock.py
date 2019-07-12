from backend.Ordering_system import OrderingSystem
from backend.Ingredient import Bun, Patty, MainsIngredient, Side, Drink
from backend.Order import Order
from backend.Inventory import Inventory
from backend.order_interface import DrinkOrder, SideOrder, MainOrder, Burger, Wrap

import pytest 

def test_add_bun():
    # How would I make different stuff have different prices
    inventory = Inventory()
    # Add buns

    inventory.add_stock_type('sesame', "bun", 0.69, 10, 1, 4, "discrete")