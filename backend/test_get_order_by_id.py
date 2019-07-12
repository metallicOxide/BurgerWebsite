from backend.Ordering_system import OrderingSystem
from backend.Ingredient import Bun, Patty, MainsIngredient, Side, Drink
from backend.Order import Order
from backend.Inventory import Inventory
from backend.order_interface import DrinkOrder, SideOrder, MainOrder, Burger, Wrap
from backend.errors import TrackOrderError
import pytest

def test_create_system(gourmet_fixture, order_fixture):
    print("\n=== Test creating the system ===\n")
    system = order_fixture
    inventory = gourmet_fixture
    assert len(system._curr_orders) == 5
    system.staff_view_orders(inventory)

def test_get_curr_order_by_id(order_fixture, gourmet_fixture):
    print("=== Test get current order by ID ===\n")
    system = order_fixture
    inventory = gourmet_fixture

    order = system.get_curr_order_by_ID(1)
    order.print_order(inventory)
    assert(order != None)

def test_get_curr_order_by_id_exception(order_fixture, gourmet_fixture):
    print("=== Test get current order by ID exception ===\n")
    system = order_fixture    
    with pytest.raises(TrackOrderError) as e:
        system.get_curr_order_by_ID(10)
    assert str(e.value) == 'Invalid ID.\n'


def test_get_completed_order_by_id(order_fixture, gourmet_fixture):
    print("=== Test get completed order by ID ===\n")
    system = order_fixture
    inventory = gourmet_fixture
    system.set_order_status("Collected", "Current", 1)

    order = system.get_completed_order_by_ID(1)
    order.print_order(inventory)
    assert(order != None)

def test_get_completed_order_by_id_exception(order_fixture, gourmet_fixture):
    print("=== Test get completed order by ID exception ===\n")
    system = order_fixture
    with pytest.raises(TrackOrderError) as e:
        system.get_completed_order_by_ID(10)
    assert str(e.value) == 'Invalid ID.\n'
