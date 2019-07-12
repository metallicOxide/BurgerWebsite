from backend.Ordering_system import OrderingSystem
from backend.Ingredient import Bun, Patty, MainsIngredient, Side, Drink
from backend.Order import Order
from backend.Inventory import Inventory
from backend.order_interface import DrinkOrder, SideOrder, MainOrder, Burger, Wrap

import pytest

def test_clear_orders_list(order_fixture, gourmet_fixture):
    print("\n=== Test clear all completed orders ===")
    system = order_fixture
    inventory = gourmet_fixture
    system.set_order_status("Collected", "Current", 0)
    system.set_order_status("Collected", "Current", 1)
    print("\nOrders in current orders list after setting 2 orders to collected\n")
    system.staff_view_orders(inventory)
    assert (len(system._curr_orders) == 3)
    print("\nOrders in completed orders list\n")
    system.staff_view_completed_orders(inventory)
    assert (len(system._completed_orders) == 2)
    system.clear_orders("Completed")
    print("\nOrders in completed orders list after clearing all orders\n")
    system.staff_view_completed_orders(inventory)
    assert (len(system._completed_orders) == 0)

def test_clear_completed_orders_list(order_fixture, gourmet_fixture):
    print("\n=== Test clear all current orders ===\n")
    system = order_fixture
    inventory = gourmet_fixture
    # set status of some orders as completed
    system.set_order_status("Collected", "Current", 0)
    system.set_order_status("Collected", "Current", 1)
    print("\nOrders in current orders list after setting 2 orders to collected\n")
    system.staff_view_orders(inventory)
    assert len(system._curr_orders) == 3
    print("\nOrders in completed orders list\n")
    system.staff_view_completed_orders(inventory)
    assert len(system._completed_orders) == 2
    system.clear_orders("Current")
    print("\nOrders in current orders list after clearing all orders\n")
    system.staff_view_orders(inventory)
    assert len(system._curr_orders) == 0

def test_clear_orders_with_ID(order_fixture, gourmet_fixture):
    print("\n=== Test clear order with specific Order ID ===\n")
    system = order_fixture
    system = order_fixture
    inventory = gourmet_fixture
    # set status of some orders as completed
    system.set_order_status("Collected", "Current", 0)
    system.set_order_status("Collected", "Current", 1)
    print("\nOrders in current orders list after setting 2 orders to collected\n")
    system.staff_view_orders(inventory)
    assert len(system._curr_orders) == 3
    print("\nOrders in completed orders list\n")
    system.staff_view_completed_orders(inventory)
    assert len(system._completed_orders) == 2
    system.clear_orders("Completed", 1)
    print("\nOrders in completed orders list after clearing order with ID 1\n")
    system.staff_view_completed_orders(inventory)
    assert len(system._completed_orders) == 1

def test_ID_exception(order_fixture, gourmet_fixture):
    print("\n=== Test Invalid ID exception ===\n")
    system = order_fixture
    system = order_fixture
    inventory = gourmet_fixture
    # set status of some orders as completed
    system.set_order_status("Collected", "Current", 0)
    system.set_order_status("Collected", "Current", 1)

    assert len(system._curr_orders) == 3
    assert len(system._completed_orders) == 2
    system.clear_orders("Collected", 100)
    assert len(system._completed_orders) == 2

def test_List_exception(order_fixture, gourmet_fixture):
    print("\n=== Test Invalid List exception ===\n")
    system = order_fixture
    system = order_fixture
    inventory = gourmet_fixture
    # set status of some orders as completed
    system.set_order_status("Collected", "Current", 0)
    system.set_order_status("Collected", "Current", 1)

    assert len(system._curr_orders) == 3
    assert len(system._completed_orders) == 2
    system.clear_orders("", 1)
    assert len(system._completed_orders) == 2
