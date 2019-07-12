from backend.Ordering_system import OrderingSystem
from backend.Ingredient import Bun, Patty, MainsIngredient, Side, Drink
from backend.Order import Order
from backend.Inventory import Inventory
from backend.order_interface import DrinkOrder, SideOrder, MainOrder, Burger, Wrap

import pytest

def test_browse(gourmet_fixture):
    print("\n=== Test Browse Menu ===")
    gourmet_fixture.browse_menu()
    assert len(gourmet_fixture.food_list) == 26
