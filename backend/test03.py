from backend.Ordering_system import OrderingSystem
from backend.Ingredient import Bun, Patty, MainsIngredient, Side, Drink
from backend.Order import Order
from backend.Inventory import Inventory
from backend.order_interface import DrinkOrder, SideOrder, MainOrder, Burger, Wrap
from backend.errors import TrackOrderError
import pytest

# Test File for Customer Order Tracking

def test_create_system(gourmet_fixture, order_fixture):
    print("\n=== Test creating the system ===\n")
    system = order_fixture
    inventory = gourmet_fixture
    assert len(system._curr_orders) == 5

    # asserts for order 1:
    main_dict = system.curr_orders[0].mains[0].ingredients     
    assert main_dict['Sesame bun'] == 2
    assert main_dict['Chicken patty'] == 1 
    assert main_dict['Tomato'] == 1
    assert main_dict['Cheddar cheese'] == 1

    side_dict = main_dict = system.curr_orders[0].sides.ingredients
    assert side_dict['6 pack nuggets'] == 1
    assert side_dict['Small fries'] == 2    

    # order number 2 
    main_dict = system.curr_orders[1].mains[0].ingredients     
    assert main_dict['Wrap'] == 1
    assert main_dict['Vegetarian patty'] == 1 
    assert main_dict['Tomato sauce'] == 1
    assert main_dict['Tomato'] == 1
    assert main_dict['Lettuce'] == 1

    drink_dict = main_dict = system.curr_orders[1].drinks.ingredients
    assert drink_dict['Vodka'] == 1

    # order number 3
    main_dict = system.curr_orders[2].mains[0].ingredients     
    assert main_dict['Burnt bun'] == 4
    assert main_dict['Tomato sauce'] == 5

    # order number 4
    main_dict = system.curr_orders[3].mains[0].ingredients     
    assert main_dict['Muffin bun'] == 3
    assert main_dict['Vegetarian patty'] == 1 
    assert main_dict['Beef patty'] == 1
    assert main_dict['Tomato sauce'] == 1
    assert main_dict['Tomato'] == 1

    side_dict = main_dict = system.curr_orders[3].sides.ingredients
    assert side_dict['6 pack nuggets'] == 1
    assert side_dict['Large fries'] == 1
    assert side_dict['Wiked wingz'] == 1  

    drink_dict = main_dict = system.curr_orders[3].drinks.ingredients
    assert drink_dict['Mtn Dew'] == 1  
    assert drink_dict['Baijiu'] == 1  
    assert drink_dict['Whiskey'] == 1  

    # order number 5
    main_dict = system.curr_orders[4].mains[0].ingredients     
    assert main_dict['Mad bun'] == 2
    assert main_dict['Vegetarian patty'] == 1 
    assert main_dict['Beef patty'] == 1
    assert main_dict['Tomato sauce'] == 1
    assert main_dict['Tomato'] == 1

    side_dict = main_dict = system.curr_orders[4].sides.ingredients
    assert side_dict['6 pack nuggets'] == 1
    assert side_dict['Large fries'] == 1

    drink_dict = main_dict = system.curr_orders[4].drinks.ingredients
    assert drink_dict['Mtn Dew'] == 1  
    
    system.staff_view_orders(inventory)

def test_get_curr_order_by_id(order_fixture, gourmet_fixture):
    print("=== Test get current order by ID ===\n")
    system = order_fixture
    inventory = gourmet_fixture

    order = system.get_curr_order_by_ID(1)
    assert(order != None)

    main_dict = order.mains[0].ingredients  
    assert main_dict['Wrap'] == 1
    assert main_dict['Vegetarian patty'] == 1 
    assert main_dict['Tomato sauce'] == 1
    assert main_dict['Tomato'] == 1
    assert main_dict['Lettuce'] == 1

    drink_dict = main_dict = order.drinks.ingredients
    assert drink_dict['Vodka'] == 1

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
    assert(order != None)
    main_dict = order.mains[0].ingredients  
    assert main_dict['Wrap'] == 1
    assert main_dict['Vegetarian patty'] == 1 
    assert main_dict['Tomato sauce'] == 1
    assert main_dict['Tomato'] == 1
    assert main_dict['Lettuce'] == 1

    drink_dict = main_dict = order.drinks.ingredients
    assert drink_dict['Vodka'] == 1

def test_get_completed_order_by_id_exception(order_fixture, gourmet_fixture):
    print("=== Test get completed order by ID exception ===\n")
    system = order_fixture
    with pytest.raises(TrackOrderError) as e:
        system.get_completed_order_by_ID(10)
    assert str(e.value) == 'Invalid ID.\n'