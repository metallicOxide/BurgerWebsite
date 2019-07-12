from backend.Ordering_system import OrderingSystem
from backend.Ingredient import Bun, Patty, MainsIngredient, Side, Drink
from backend.Order import Order
from backend.Inventory import Inventory
from backend.order_interface import DrinkOrder, SideOrder, MainOrder, Burger, Wrap
from backend.errors import StatusError

import pytest

def test_set_order_status(order_fixture, gourmet_fixture):
    print("=== Test set current order status ===\n")
    system = order_fixture
    inventory = gourmet_fixture
    print ("\nList of Current Orders\n")
    system.staff_view_orders(inventory)
    assert len(system.curr_orders) == 5
    # set status of order as completed
    system.set_order_status("Collected", "Current", 1)
    print ("\nList of Current Orders after setting order as Collected\n")
    system.staff_view_orders(inventory)
    assert len(system.curr_orders) == 4
    print("\nList of Completed Orders after setting order as Collected\n")
    system.staff_view_completed_orders(inventory)
    assert len(system.completed_orders) == 1
    assert system.completed_orders[0].status == "Collected"

def test_set_completed_order_status(order_fixture, gourmet_fixture):
    print("\n=== Test set completed order status ===")
    system = order_fixture
    inventory = gourmet_fixture
    system.set_order_status("Collected", "Current", 1)
    print ("\nList of Current Orders\n")
    assert len(system.curr_orders) == 4
    system.staff_view_orders(inventory)
    print("\nList of Completed Orders\n")
    system.staff_view_completed_orders(inventory)
    assert len(system.completed_orders) == 1
    # set status of order as completed
    system.set_order_status("Preparing", "Completed", 1)
    assert len(system.completed_orders) == 0
    assert len(system.curr_orders) == 5
    assert order_fixture.get_curr_order_by_ID(1).status == "Preparing"
    print("\nList of Current Orders after reverting order in Completed List\n")
    system.staff_view_orders(inventory)

def test_set_current_order_status_empty_exception(order_fixture, gourmet_fixture):
    print("\n=== Test set order status empty status exception===")
    system = order_fixture
    with pytest.raises(StatusError) as e:
        system.set_order_status("", "Current", 1)
    assert str(e.value) == "Please provide an Order Status from the drop down list.\n"
    assert len(system.curr_orders) == 5

def test_set_current_order_status_incorrect_exception(order_fixture, gourmet_fixture):
    print("\n=== Test set order status incorrect status exception===")
    system = order_fixture
    with pytest.raises(StatusError) as e:
        system.set_order_status("HELLO", "Current", 1)
    assert str(e.value) == "Please provide an Order Status from the drop down list.\n"
    assert len(system.curr_orders) == 5

def test_set_current_order_list_incorrect_exception(order_fixture, gourmet_fixture):
    print("\n=== Test set order status empty list exception===")
    system = order_fixture
    with pytest.raises(StatusError) as e:
        system.set_order_status("Collected", "", 1)
    assert str(e.value) == "Please specify if the order is current or completed.\n"
    assert len(system.curr_orders) == 5

