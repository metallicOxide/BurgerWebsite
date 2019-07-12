from backend.Ordering_system import OrderingSystem
from backend.Ingredient import Bun, Patty, MainsIngredient, Side, Drink
from backend.Order import Order
from backend.Inventory import Inventory
from backend.order_interface import DrinkOrder, SideOrder, MainOrder, Burger, Wrap

import pytest

def test_view_current_orders(order_fixture, gourmet_fixture):
    inventory = gourmet_fixture
    system = order_fixture
    print("\n=== Test Staff View Current Orders ===\n")
    system.staff_view_orders(inventory)
    assert len(system.curr_orders) == 5

def test_view_completed_orders(order_fixture, gourmet_fixture):
    inventory = gourmet_fixture
    system = order_fixture
    system.set_order_status("Collected", "Current", 0)
    system.set_order_status("Collected", "Current", 1)
    print("\n=== Test Staff View Completed Orders ===\n")
    system.staff_view_completed_orders(inventory)
    assert len(system.curr_orders) == 3
    assert len(system.completed_orders) == 2
