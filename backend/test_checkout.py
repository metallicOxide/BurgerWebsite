from backend.Ordering_system import OrderingSystem
from backend.Ingredient import Bun, Patty, MainsIngredient, Side, Drink
from backend.Order import Order
from backend.Inventory import Inventory
from backend.order_interface import DrinkOrder, SideOrder, MainOrder, Burger, Wrap
from backend.errors import OrderError

import pytest

def test_checkout_basic(gourmet_fixture):
    print("~~~~~~~~~~~ checkout basic ~~~~~~~~~~~~")
    inv = gourmet_fixture
    system = OrderingSystem()

    main = {}
    main[inv.get_ingredient('sesame bun').name] = 2
    main[inv.get_ingredient('chicken patty').name] = 1
    main[inv.get_ingredient('tomato').name] = 1 
    main[inv.get_ingredient('Cheddar cheese').name] = 1 

    side = {}
    side[inv.get_ingredient('6 pack nuggets').name] = 1
    side[inv.get_ingredient('small fries').name] = 2

    drink = {}
    drink[inv.get_ingredient('cokain').name] = 2 
    drink[inv.get_ingredient('sake').name] = 1

    mains = []
    mains.append(main)

    order_ID = system.checkout(mains, side, drink, inv)
    # assert(inv.food_dict[item] == [insert number here])
    order = system.get_curr_order_by_ID(order_ID)
    main_ingredient = order.mains[0].ingredients
    assert main_ingredient['Sesame bun'] == 2
    assert main_ingredient['Chicken patty'] == 1
    assert main_ingredient['Tomato'] == 1
    assert main_ingredient['Cheddar cheese'] == 1

    side_ingredient = order.sides.ingredients
    assert side_ingredient['6 pack nuggets'] == 1
    assert side_ingredient['Small fries'] == 2

    drink_ingredient = order.drinks.ingredients
    assert drink_ingredient['Cokain'] == 2
    assert drink_ingredient['Sake'] == 1
    order.print_order(inv)


def test_checkout_basic_inventory_update(gourmet_fixture):
    print("~~~~~~~~~~~ checkout basic ~~~~~~~~~~~~")
    inv = gourmet_fixture
    system = OrderingSystem()

    main = {}
    main[inv.get_ingredient('sesame bun').name] = 2
    main[inv.get_ingredient('chicken patty').name] = 1
    main[inv.get_ingredient('tomato').name] = 1 
    main[inv.get_ingredient('Cheddar cheese').name] = 1 

    side = {}
    side[inv.get_ingredient('6 pack nuggets').name] = 1
    side[inv.get_ingredient('small fries').name] = 2

    drink = {}
    drink[inv.get_ingredient('cokain').name] = 2 
    drink[inv.get_ingredient('sake').name] = 1

    mains = []
    mains.append(main)

    system.checkout(mains, side, drink, inv)
    # assert(inv.food_dict[item] == [insert number here])
    # check quantity left in inventory after checking out
    assert gourmet_fixture.get_stock_quantity('Sesame bun') == 8
    assert gourmet_fixture.get_stock_quantity('Chicken patty') == 19
    assert gourmet_fixture.get_stock_quantity('Tomato') == 68
    assert gourmet_fixture.get_stock_quantity('Cheddar cheese') == 68
    assert gourmet_fixture.get_stock_quantity('6 pack nuggets') == 98
    assert gourmet_fixture.get_stock_quantity('Small fries') == 95
    assert gourmet_fixture.get_stock_quantity('Cokain') == 9
    assert gourmet_fixture.get_stock_quantity('Sake') == 10

def test_checkout_two_main(gourmet_fixture):
    print("~~~~~~~~~~~ checkout two main ~~~~~~~~~~~~")
    inv = gourmet_fixture
    system = OrderingSystem()

    main = {}
    main[inv.get_ingredient('sesame bun').name] = 2
    main[inv.get_ingredient('chicken patty').name] = 1
    main[inv.get_ingredient('tomato').name] = 1 
    main[inv.get_ingredient('Cheddar cheese').name] = 1 

    main_two = {}
    main_two[inv.get_ingredient('Mad bun').name] = 2
    main_two[inv.get_ingredient('beef patty').name] = 2
    main_two[inv.get_ingredient('lettuce').name] = 3
    main_two[inv.get_ingredient('Swiss cheese').name] = 5

    side = {}
    side[inv.get_ingredient('6 pack nuggets').name] = 1
    side[inv.get_ingredient('small fries').name] = 2

    drink = {}
    drink[inv.get_ingredient('cokain').name] = 2 
    drink[inv.get_ingredient('sake').name] = 1

    mains = []
    mains.append(main)
    mains.append(main_two)

    order_ID = system.checkout(mains, side, drink, inv)
    # assert(inv.food_dict[item] == [insert number here])
    order = system.get_curr_order_by_ID(order_ID)
    main_ingredient = order.mains[0].ingredients
    assert main_ingredient['Sesame bun'] == 2
    assert main_ingredient['Chicken patty'] == 1
    assert main_ingredient['Tomato'] == 1
    assert main_ingredient['Cheddar cheese'] == 1

    main_ingredient = order.mains[1].ingredients
    assert main_ingredient['Mad bun'] == 2
    assert main_ingredient['Beef patty'] == 2
    assert main_ingredient['Lettuce'] == 3
    assert main_ingredient['Swiss Cheese'] == 5

    side_ingredient = order.sides.ingredients
    assert side_ingredient['6 pack nuggets'] == 1
    assert side_ingredient['Small fries'] == 2

    drink_ingredient = order.drinks.ingredients
    assert drink_ingredient['Cokain'] == 2
    assert drink_ingredient['Sake'] == 1
    order.print_order(inv)

def test_checkout_two_main_inventory_update(gourmet_fixture):
    print("~~~~~~~~~~~ checkout two main ~~~~~~~~~~~~")
    inv = gourmet_fixture
    system = OrderingSystem()

    main = {}
    main[inv.get_ingredient('sesame bun').name] = 2
    main[inv.get_ingredient('chicken patty').name] = 1
    main[inv.get_ingredient('tomato').name] = 1 
    main[inv.get_ingredient('Cheddar cheese').name] = 1 

    main_two = {}
    main_two[inv.get_ingredient('Mad bun').name] = 2
    main_two[inv.get_ingredient('beef patty').name] = 2
    main_two[inv.get_ingredient('lettuce').name] = 3
    main_two[inv.get_ingredient('Swiss cheese').name] = 5

    side = {}
    side[inv.get_ingredient('6 pack nuggets').name] = 1
    side[inv.get_ingredient('small fries').name] = 2

    drink = {}
    drink[inv.get_ingredient('cokain').name] = 2 
    drink[inv.get_ingredient('sake').name] = 1

    mains = []
    mains.append(main)
    mains.append(main_two)

    system.checkout(mains, side, drink, inv)
    assert gourmet_fixture.get_stock_quantity('Sesame bun') == 8
    assert gourmet_fixture.get_stock_quantity('Chicken patty') == 19
    assert gourmet_fixture.get_stock_quantity('Tomato') == 68
    assert gourmet_fixture.get_stock_quantity('Cheddar cheese') == 68
    assert gourmet_fixture.get_stock_quantity('Mad bun') == 8
    assert gourmet_fixture.get_stock_quantity('Beef patty') == 18
    assert gourmet_fixture.get_stock_quantity('Lettuce') == 66
    assert gourmet_fixture.get_stock_quantity('Swiss Cheese') == 64
    assert gourmet_fixture.get_stock_quantity('6 pack nuggets') == 98
    assert gourmet_fixture.get_stock_quantity('Small fries') == 95
    assert gourmet_fixture.get_stock_quantity('Cokain') == 9
    assert gourmet_fixture.get_stock_quantity('Sake') == 10

def test_checkout_multiple_orders(gourmet_fixture):
    print("~~~~~~~~~~~ checkout multiple orders ~~~~~~~~~~~~")
    inv = gourmet_fixture
    system = OrderingSystem()

    main = {}
    main[inv.get_ingredient('sesame bun').name] = 2
    main[inv.get_ingredient('chicken patty').name] = 1
    main[inv.get_ingredient('tomato').name] = 1 
    main[inv.get_ingredient('Cheddar cheese').name] = 1 

    side = {}
    side[inv.get_ingredient('6 pack nuggets').name] = 1
    side[inv.get_ingredient('small fries').name] = 2

    mains = []
    mains.append(main)

    order_ID = system.checkout(mains, side, None, inv)
    assert(len(system._curr_orders) == 1)
    assert order_ID == 0
    order = system.get_curr_order_by_ID(order_ID)
    main_ingredient = order.mains[0].ingredients
    assert main_ingredient['Sesame bun'] == 2
    assert main_ingredient['Chicken patty'] == 1
    assert main_ingredient['Tomato'] == 1
    assert main_ingredient['Cheddar cheese'] == 1

    side_ingredient = order.sides.ingredients
    assert side_ingredient['6 pack nuggets'] == 1
    assert side_ingredient['Small fries'] == 2
    order.print_order(inv)


    main = {}
    main[inv.get_ingredient('wrap').name] = 1 
    main[inv.get_ingredient('vegetarian patty').name] = 1
    main[inv.get_ingredient('tomato sauce').name] = 1
    main[inv.get_ingredient('lettuce').name] = 1
    main[inv.get_ingredient('tomato').name] = 1

    drink = {}
    drink[inv.get_ingredient('vodka').name] = 1

    mains = []
    mains.append(main)

    order_ID = system.checkout(mains, None, drink, inv)
    assert(len(system._curr_orders) == 2)
    assert order_ID == 1
    order = system.get_curr_order_by_ID(order_ID)
    main_ingredient = order.mains[0].ingredients
    assert main_ingredient['Wrap'] == 1
    assert main_ingredient['Vegetarian patty'] == 1
    assert main_ingredient['Lettuce'] == 1
    assert main_ingredient['Tomato'] == 1

    drink_ingredient = order.drinks.ingredients
    assert drink_ingredient['Vodka'] == 1
    order.print_order(inv)

    main = {}
    main[inv.get_ingredient('burnt bun').name] = 3
    main[inv.get_ingredient('tomato sauce').name] = 5 

    mains = []
    mains.append(main)

    order_ID = system.checkout(mains, '', '', inv)
    assert(len(system._curr_orders) == 3)

    order = system.get_curr_order_by_ID(order_ID)
    main_ingredient = order.mains[0].ingredients
    assert main_ingredient['Burnt bun'] == 3
    assert main_ingredient['Tomato sauce'] == 5
    order.print_order(inv)

    main = {}
    main[inv.get_ingredient('muffin bun').name] = 3
    main[inv.get_ingredient('Vegetarian patty').name] = 1
    main[inv.get_ingredient('beef patty').name] = 1
    main[inv.get_ingredient('tomato sauce').name] = 1
    main[inv.get_ingredient('tomato').name] = 1
 
    side = {}
    side[inv.get_ingredient('6 pack nuggets').name] = 1 
    side[inv.get_ingredient('large fries').name] = 1 
    side[inv.get_ingredient('wiked wingz').name] = 1

    drink = {}
    drink[inv.get_ingredient('Mtn dew').name] = 1
    drink[inv.get_ingredient('baijiu').name] = 1
    drink[inv.get_ingredient('whiskey').name] = 1

    mains = []
    mains.append(main)

    order_ID = system.checkout(mains, side, drink, inv)
    assert(len(system._curr_orders) == 4)

    order = system.get_curr_order_by_ID(order_ID)
    main_ingredient = order.mains[0].ingredients
    assert main_ingredient['Muffin bun'] == 3
    assert main_ingredient['Vegetarian patty'] == 1
    assert main_ingredient['Beef patty'] == 1
    assert main_ingredient['Tomato sauce'] == 1
    assert main_ingredient['Tomato'] == 1

    side_ingredient = order.sides.ingredients
    assert side_ingredient['6 pack nuggets'] == 1
    assert side_ingredient['Large fries'] == 1
    assert side_ingredient['Wiked wingz'] == 1

    drink_ingredient = order.drinks.ingredients
    assert drink_ingredient['Mtn Dew'] == 1
    assert drink_ingredient['Baijiu'] == 1
    assert drink_ingredient['Whiskey'] == 1

    order.print_order(inv)

def test_checkout_multiple_orders_update_inventory(gourmet_fixture):
    print("~~~~~~~~~~~ checkout two mains ~~~~~~~~~~~~")
    inv = gourmet_fixture
    system = OrderingSystem()

    # order number 1 
    main = {}
    main[inv.get_ingredient('sesame bun').name] = 2
    main[inv.get_ingredient('chicken patty').name] = 1
    main[inv.get_ingredient('tomato').name] = 1 
    main[inv.get_ingredient('Cheddar cheese').name] = 1 

    side = {}
    side[inv.get_ingredient('6 pack nuggets').name] = 1
    side[inv.get_ingredient('small fries').name] = 2

    mains = []
    mains.append(main)

    system.checkout(mains, side, None, inv)
    assert gourmet_fixture.get_stock_quantity('Sesame bun') == 8
    assert gourmet_fixture.get_stock_quantity('Chicken patty') == 19
    assert gourmet_fixture.get_stock_quantity('Tomato') == 68
    assert gourmet_fixture.get_stock_quantity('Cheddar cheese') == 68
    assert gourmet_fixture.get_stock_quantity('6 pack nuggets') == 98
    assert gourmet_fixture.get_stock_quantity('Small fries') == 95

    # order number 2
    main = {}
    main[inv.get_ingredient('wrap').name] = 1 
    main[inv.get_ingredient('vegetarian patty').name] = 1 
    main[inv.get_ingredient('tomato sauce').name] = 1
    main[inv.get_ingredient('lettuce').name] = 1
    main[inv.get_ingredient('tomato').name] = 1

    drink = {}
    drink[inv.get_ingredient('vodka').name] = 1 

    mains = []
    mains.append(main)

    system.checkout(mains, None, drink, inv)
    assert gourmet_fixture.get_stock_quantity('Wrap') == 11
    assert gourmet_fixture.get_stock_quantity('Vegetarian patty') == 19
    assert gourmet_fixture.get_stock_quantity('Tomato sauce') == 68
    assert gourmet_fixture.get_stock_quantity('Lettuce') == 68
    assert gourmet_fixture.get_stock_quantity('Tomato') == 67
    assert gourmet_fixture.get_stock_quantity('Vodka') == 10

    # order number 3
    main = {}
    main[inv.get_ingredient('burnt bun').name] = 3
    main[inv.get_ingredient('tomato sauce').name] = 5 

    mains = []
    mains.append(main)

    system.checkout(mains, '', '', inv)
    assert gourmet_fixture.get_stock_quantity('Tomato sauce') == 63
    assert gourmet_fixture.get_stock_quantity('Burnt bun') == 7

    # order number 4
    main = {}
    main[inv.get_ingredient('muffin bun').name] = 3
    main[inv.get_ingredient('Vegetarian patty').name] = 1
    main[inv.get_ingredient('beef patty').name] = 1
    main[inv.get_ingredient('tomato sauce').name] = 1
    main[inv.get_ingredient('tomato').name] = 1

    side = {}
    side[inv.get_ingredient('6 pack nuggets').name] = 1 
    side[inv.get_ingredient('large fries').name] = 1 
    side[inv.get_ingredient('wiked wingz').name] = 1

    drink = {}
    drink[inv.get_ingredient('Mtn dew').name] = 1
    drink[inv.get_ingredient('baijiu').name] = 1
    drink[inv.get_ingredient('whiskey').name] = 1

    mains = []
    mains.append(main)

    system.checkout(mains, side, drink, inv)
    assert gourmet_fixture.get_stock_quantity('Muffin bun') == 7
    assert gourmet_fixture.get_stock_quantity('Vegetarian patty') == 18
    assert gourmet_fixture.get_stock_quantity('Beef patty') == 19
    assert gourmet_fixture.get_stock_quantity('Tomato sauce') == 62
    assert gourmet_fixture.get_stock_quantity('Tomato') == 66

    assert gourmet_fixture.get_stock_quantity('6 pack nuggets') == 95
    assert gourmet_fixture.get_stock_quantity('Large fries') == 98
    assert gourmet_fixture.get_stock_quantity('Wiked Wingz') == 98

    assert gourmet_fixture.get_stock_quantity('Mtn dew') == 10
    assert gourmet_fixture.get_stock_quantity('Baijiu') == 10
    assert gourmet_fixture.get_stock_quantity('Whiskey') == 10

def test_checkout_empty_mains(gourmet_fixture):
    print("~~~~~~~~~~~ checkout empty side ~~~~~~~~~~~~")
    inv = gourmet_fixture
    system = OrderingSystem()
   
    side = {}
    side[inv.get_ingredient('6 pack nuggets').name] = 1 
    side[inv.get_ingredient('large fries').name] = 1 
    side[inv.get_ingredient('wiked wingz').name] = 1

    drink = {}
    drink[inv.get_ingredient('Mtn dew').name] = 1
    drink[inv.get_ingredient('baijiu').name] = 1
    drink[inv.get_ingredient('whiskey').name] = 1


    order_ID = system.checkout(None, side, drink, inv)
    assert(len(system._curr_orders) == 1)
    order = system.get_curr_order_by_ID(order_ID)
    side_ingredient = order.sides.ingredients
    assert side_ingredient['6 pack nuggets'] == 1
    assert side_ingredient['Large fries'] == 1
    assert side_ingredient['Wiked wingz'] == 1

    drink_ingredient = order.drinks.ingredients
    assert drink_ingredient['Mtn Dew'] == 1
    assert drink_ingredient['Baijiu'] == 1
    assert drink_ingredient['Whiskey'] == 1
    order.print_order(inv)

        
def test_checkout_empty_mains_update_inventory(gourmet_fixture):
    print("~~~~~~~~~~~ checkout empty side ~~~~~~~~~~~~")
    inv = gourmet_fixture
    system = OrderingSystem()
   
    side = {}
    side[inv.get_ingredient('6 pack nuggets').name] = 1 
    side[inv.get_ingredient('large fries').name] = 1 
    side[inv.get_ingredient('wiked wingz').name] = 1

    drink = {}
    drink[inv.get_ingredient('Mtn dew').name] = 1
    drink[inv.get_ingredient('baijiu').name] = 1
    drink[inv.get_ingredient('whiskey').name] = 1

    system.checkout(None, side, drink, inv)
    assert gourmet_fixture.get_stock_quantity('6 pack nuggets') == 98
    assert gourmet_fixture.get_stock_quantity('Large fries') == 98
    assert gourmet_fixture.get_stock_quantity('Wiked Wingz') == 98
    assert gourmet_fixture.get_stock_quantity('Mtn dew') == 10
    assert gourmet_fixture.get_stock_quantity('Baijiu') == 10
    assert gourmet_fixture.get_stock_quantity('Whiskey') == 10

def test_checkout_empty_sides(gourmet_fixture):
    print("~~~~~~~~~~~ checkout empty side ~~~~~~~~~~~~")
    inv = gourmet_fixture
    system = OrderingSystem()

    main = {}
    main[inv.get_ingredient('sesame bun').name] = 2
    main[inv.get_ingredient('chicken patty').name] = 1
    main[inv.get_ingredient('tomato').name] = 1 
    main[inv.get_ingredient('Cheddar cheese').name] = 1 
    
    drink = {}
    drink[inv.get_ingredient('Mtn dew').name] = 1
    drink[inv.get_ingredient('baijiu').name] = 1
    drink[inv.get_ingredient('whiskey').name] = 1

    mains = []
    mains.append(main)

    system.checkout(mains, None, drink, inv)
    assert gourmet_fixture.get_stock_quantity('Sesame bun') == 8
    assert gourmet_fixture.get_stock_quantity('Chicken patty') == 19
    assert gourmet_fixture.get_stock_quantity('Tomato') == 68
    assert gourmet_fixture.get_stock_quantity('Cheddar cheese') == 68
    assert gourmet_fixture.get_stock_quantity('Mtn dew') == 10
    assert gourmet_fixture.get_stock_quantity('Baijiu') == 10
    assert gourmet_fixture.get_stock_quantity('Whiskey') == 10


def test_checkout_empty_sides_update_inventory(gourmet_fixture):
    print("~~~~~~~~~~~ checkout empty side ~~~~~~~~~~~~")
    inv = gourmet_fixture
    system = OrderingSystem()

    main = {}
    main[inv.get_ingredient('sesame bun').name] = 2
    main[inv.get_ingredient('chicken patty').name] = 1
    main[inv.get_ingredient('tomato').name] = 1 
    main[inv.get_ingredient('Cheddar cheese').name] = 1 
 
    drink = {}
    drink[inv.get_ingredient('Mtn dew').name] = 1
    drink[inv.get_ingredient('baijiu').name] = 1
    drink[inv.get_ingredient('whiskey').name] = 1

    mains = []
    mains.append(main)

    order_ID = system.checkout(mains, None, drink, inv)
    assert(len(system._curr_orders) == 1)
    order = system.get_curr_order_by_ID(order_ID)

    main_ingredient = order.mains[0].ingredients
    assert main_ingredient['Sesame bun'] == 2
    assert main_ingredient['Chicken patty'] == 1
    assert main_ingredient['Tomato'] == 1
    assert main_ingredient['Cheddar cheese'] == 1

    drink_ingredient = order.drinks.ingredients
    assert drink_ingredient['Mtn Dew'] == 1
    assert drink_ingredient['Baijiu'] == 1
    assert drink_ingredient['Whiskey'] == 1
    
    order.print_order(inv)

def test_checkout_empty_drinks(gourmet_fixture):
    print("~~~~~~~~~~~ checkout empty drinks ~~~~~~~~~~~~")
    inv = gourmet_fixture
    system = OrderingSystem()

    main = {}
    main[inv.get_ingredient('sesame bun').name] = 2
    main[inv.get_ingredient('chicken patty').name] = 1
    main[inv.get_ingredient('tomato').name] = 1 
    main[inv.get_ingredient('Cheddar cheese').name] = 1 
   
    side = {}
    side[inv.get_ingredient('6 pack nuggets').name] = 1 
    side[inv.get_ingredient('large fries').name] = 1 
    side[inv.get_ingredient('wiked wingz').name] = 1

    mains = []
    mains.append(main)

    order_ID = system.checkout(mains, side, None, inv)
    assert(len(system._curr_orders) == 1)
    order = system.get_curr_order_by_ID(order_ID)
    main_ingredient = order.mains[0].ingredients
    assert main_ingredient['Sesame bun'] == 2
    assert main_ingredient['Chicken patty'] == 1
    assert main_ingredient['Tomato'] == 1
    assert main_ingredient['Cheddar cheese'] == 1

    side_ingredient = order.sides.ingredients
    assert side_ingredient['6 pack nuggets'] == 1
    assert side_ingredient['Large fries'] == 1
    assert side_ingredient['Wiked wingz'] == 1

    order.print_order(inv)

def test_checkout_empty_drinks_update_inventory(gourmet_fixture):
    print("~~~~~~~~~~~ checkout empty side ~~~~~~~~~~~~")
    inv = gourmet_fixture
    system = OrderingSystem()

    main = {}
    main[inv.get_ingredient('sesame bun').name] = 2
    main[inv.get_ingredient('chicken patty').name] = 1
    main[inv.get_ingredient('tomato').name] = 1 
    main[inv.get_ingredient('Cheddar cheese').name] = 1 
   
    side = {}
    side[inv.get_ingredient('6 pack nuggets').name] = 1 
    side[inv.get_ingredient('large fries').name] = 1 
    side[inv.get_ingredient('wiked wingz').name] = 1

    mains = []
    mains.append(main)

    system.checkout(mains, side, None, inv)
    assert gourmet_fixture.get_stock_quantity('Sesame bun') == 8
    assert gourmet_fixture.get_stock_quantity('Chicken patty') == 19
    assert gourmet_fixture.get_stock_quantity('Tomato') == 68
    assert gourmet_fixture.get_stock_quantity('Cheddar cheese') == 68
    assert gourmet_fixture.get_stock_quantity('6 pack nuggets') == 98
    assert gourmet_fixture.get_stock_quantity('Large fries') == 98
    assert gourmet_fixture.get_stock_quantity('Wiked Wingz') == 98


def test_checkout_exception_all_empty(gourmet_fixture):
    print("~~~~~~~~~~~ checkout all empty ~~~~~~~~~~~~")
    inv = gourmet_fixture
    system = OrderingSystem()
    with pytest.raises(OrderError) as e:
        system.checkout(None, None, None, inv)
    assert str(e.value) == "Invalid order, please add in a main/side/drink.\n"

def test_checkout_exception_empty_inventory(gourmet_fixture):
    print("~~~~~~~~~~~ checkout all empty ~~~~~~~~~~~~")
    inv = gourmet_fixture
    system = OrderingSystem()

    main = {}
    main[inv.get_ingredient('sesame bun').name] = 2
    main[inv.get_ingredient('chicken patty').name] = 1
    main[inv.get_ingredient('tomato').name] = 1 
    main[inv.get_ingredient('Cheddar cheese').name] = 1 

    side = {}
    side[inv.get_ingredient('6 pack nuggets').name] = 1 
    side[inv.get_ingredient('large fries').name] = 1 
    side[inv.get_ingredient('wiked wingz').name] = 1

    drink = {}
    drink[inv.get_ingredient('Mtn dew').name] = 1
    drink[inv.get_ingredient('baijiu').name] = 1
    drink[inv.get_ingredient('whiskey').name] = 1

    mains = []
    mains.append(main)

    with pytest.raises(OrderError) as e:
        system.checkout(mains, side, drink, None)
    assert str(e.value) == "Invalid Inventory specified.\n"

def test_checkout_exception_no_inventory(gourmet_fixture):
    print("~~~~~~~~~~~ checkout all empty ~~~~~~~~~~~~")
    inv = gourmet_fixture
    system = OrderingSystem()

    main = {}
    main[inv.get_ingredient('sesame bun').name] = 2
    main[inv.get_ingredient('chicken patty').name] = 1
    main[inv.get_ingredient('tomato').name] = 1 
    main[inv.get_ingredient('Cheddar cheese').name] = 1 

    side = {}
    side[inv.get_ingredient('6 pack nuggets').name] = 1 
    side[inv.get_ingredient('large fries').name] = 1 
    side[inv.get_ingredient('wiked wingz').name] = 1

    drink = {}
    drink[inv.get_ingredient('Mtn dew').name] = 1
    drink[inv.get_ingredient('baijiu').name] = 1
    drink[inv.get_ingredient('whiskey').name] = 1

    with pytest.raises(OrderError) as e:
        system.checkout(main, side, drink, '')
    assert str(e.value) == "Invalid Inventory specified.\n"

def test_checkout_all_empty(gourmet_fixture):
    print("~~~~~~~~~~~ checkout all empty ~~~~~~~~~~~~")
    inv = gourmet_fixture
    system = OrderingSystem()
    side = {}
    drink = {}
    mains = []
    with pytest.raises(OrderError) as e:
        system.checkout(mains, side, drink, inv)
    assert str(e.value) == "Invalid order, please add in a main/side/drink.\n"


    
