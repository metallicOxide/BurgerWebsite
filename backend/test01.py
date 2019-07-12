from backend.Ordering_system import OrderingSystem
from backend.Ingredient import Bun, Patty, MainsIngredient, Side, Drink
from backend.Order import Order
from backend.Inventory import Inventory
from backend.order_interface import DrinkOrder, SideOrder, MainOrder, Burger, Wrap
from backend.errors import OrderError

import pytest


# Test File for Making an Order

# Test Add to Order

class IdGenerator():

    def __init__(self, id):
        self._id = id

    def next(self):
        self._id += 1
        return self._id

def test_create_system(gourmet_fixture, order_fixture):
    print("\n=== Test creating the system ===\n")
    system = order_fixture
    inventory = gourmet_fixture
    assert len(system._curr_orders) == 5
    system.staff_view_orders(inventory)

def test_get_stock_quantity(gourmet_fixture):
    # test bun
    amount = gourmet_fixture.get_stock_quantity("sesame bun")
    assert amount == 10
    # test wrap
    amount = gourmet_fixture.get_stock_quantity("wrap")
    assert amount == 12
    # test chicken patty
    amount = gourmet_fixture.get_stock_quantity("chicken patty")
    assert amount == 20
    # test Tomato sauce
    amount = gourmet_fixture.get_stock_quantity("tomato sauce")
    assert amount == 69
    # test base burgers
    amount = gourmet_fixture.get_stock_quantity("base")
    assert amount == 50
    # test side
    amount = gourmet_fixture.get_stock_quantity("Small fries")
    assert amount == 101
    # test drinks
    amount = gourmet_fixture.get_stock_quantity("sake")
    assert amount == 11

def test_print_fixture(gourmet_fixture):

    print("\n~~~~~~~~~~~~~~ printing food list ~~~~~~~~~~~~~~~~:\n")
    print(gourmet_fixture.food_list)
    print("\n")
    for food in gourmet_fixture.food_list:
        print(food.name)
    print("printing food dictionary\n")
    print(gourmet_fixture.food_dict)
    print("\n")
    for key in gourmet_fixture.food_dict:
        print(key)
    assert(len(gourmet_fixture.food_list) == 26)

def test_get_ingredient(gourmet_fixture):
    print("\n~~~~~~~~~~~~ testing get ingredient ~~~~~~~~~~~~~~~~\n")
    print("getting a cokain drink")
    drink = gourmet_fixture.get_ingredient('Cokain')
    assert drink.name == 'Cokain'
    assert drink.price == 69
    print("got: ", drink)

    print("\ngetting a COKAIN drink but i want all caps!")
    drink = gourmet_fixture.get_ingredient('COKAIN')
    assert drink.name == 'Cokain'
    assert drink.price == 69
    print('got: ', drink)

    print("\ngetting a 6 pack chicken nugs")
    side = gourmet_fixture.get_ingredient('6 pack nuggets')
    assert side.name == '6 pack nuggets'
    assert side.price == 4.2
    print("got: ", side)

    print("\ngetting tomato")
    item = gourmet_fixture.get_ingredient('tomato')
    assert item.name == 'Tomato'
    assert item.price == 0.66
    print("got: ", item)

    print("\ngetting chicken patty")
    item = gourmet_fixture.get_ingredient('chicken patty')
    assert item.name == 'Chicken patty'
    assert item.price == 6.66
    print("got: ", item)

    print("\ngetting sesame bun")
    item = gourmet_fixture.get_ingredient('sesame bun')
    assert item.name == 'Sesame bun'
    assert item.price == 0.69
    print("got: ", item)


def test_make_main_order(gourmet_fixture):
    print("\n~~~~~~~~~ test making order ~~~~~~~~~~~~~~")
    inv = gourmet_fixture
    IDgen = IdGenerator(0)
    ID = IDgen.next()
    system = OrderingSystem()
    order = system.create_order(ID)

    main_one = {}
    print("adding 2 sesame bun")
    main_one[inv.get_ingredient('sesame bun').name] = 2
    print("adding chicken patty")
    main_one[inv.get_ingredient('chicken patty').name] = 1
    print("adding tomato")
    main_one[inv.get_ingredient('tomato').name] = 1
    print("adding Cheddar cheese\n")
    main_one[inv.get_ingredient('cheddar cheese').name] = 1
    system.add_to_order(ID, main_one, inv)

    print("printing out order after adding main number one")
    order.print_order(inv)
    assert order.calculate_order_price(inv) == 12.36
    main_one_ingredients = order.mains[0].ingredients
    assert main_one_ingredients['Sesame bun'] == 2
    assert main_one_ingredients['Chicken patty'] == 1
    assert main_one_ingredients['Tomato'] == 1
    assert main_one_ingredients['Cheddar cheese'] == 1


def test_make_two_main_order(gourmet_fixture):
    print("\n~~~~~~~~~ test make two main order ~~~~~~~~~~~~~~")
    inv = gourmet_fixture
    IDgen = IdGenerator(0)
    ID = IDgen.next()
    system = OrderingSystem()
    order = system.create_order(ID)

    main_one = {}
    print("adding 2 sesame bun")
    main_one[inv.get_ingredient('sesame bun').name] = 2
    print("adding chicken patty")
    main_one[inv.get_ingredient('chicken patty').name] = 1
    print("adding tomato")
    main_one[inv.get_ingredient('tomato').name] = 1
    print("adding Cheddar cheese\n")
    main_one[inv.get_ingredient('Cheddar cheese').name] = 1 
    system.add_to_order(ID, main_one, inv)
    assert order.calculate_order_price(inv) == 12.36

    main_two = {}
    print("adding wrap")
    main_two[inv.get_ingredient('wrap').name] = 1
    print("adding 2 beef patty")
    main_two[inv.get_ingredient('beef patty').name] = 2
    print("adding tomoato sauce")
    main_two[inv.get_ingredient('tomato sauce').name] = 1
    print("adding swiss cheese")
    main_two[inv.get_ingredient('swiss cheese').name] = 1
    system.add_to_order(ID, main_two, inv)
    print("printing out order after adding main number two")
    order.print_order(inv)
    assert order.calculate_order_price(inv) == 37.19

    main_two_ingredients = order.mains[1].ingredients
    assert main_two_ingredients['Wrap'] == 1
    assert main_two_ingredients['Beef patty'] == 2
    assert main_two_ingredients['Tomato sauce'] == 1
    assert main_two_ingredients['Swiss Cheese'] == 1

    main_one_ingredients = order.mains[0].ingredients
    assert main_one_ingredients['Sesame bun'] == 2
    assert main_one_ingredients['Chicken patty'] == 1
    assert main_one_ingredients['Tomato'] == 1
    assert main_one_ingredients['Cheddar cheese'] == 1


def test_add_side(gourmet_fixture):
    print("\n~~~~~~~~~ test make side order~~~~~~~~~~~~~~")
    inv = gourmet_fixture
    IDgen = IdGenerator(0)
    ID = IDgen.next()
    system = OrderingSystem()
    order = system.create_order(ID)

    side = {}
    print("adding chicken nuggests 6")
    side[inv.get_ingredient('6 pack nuggets').name] = 1
    print("adding 2 small fries")
    side[inv.get_ingredient('small fries').name] = 2
    system.add_to_order(ID, side, inv)
    print("printing out order after adding side")
    order.print_order(inv)

    side = order.sides.ingredients
    assert side['6 pack nuggets'] == 1
    assert side['Small fries'] == 2
    assert(round(order.calculate_order_price(inv),2) == 12.6)

def test_add_drink(gourmet_fixture):
    print("\n ~~~~~~~ test make drink order ~~~~~~~~~~~~~")
    inv = gourmet_fixture
    IDgen = IdGenerator(0)
    ID = IDgen.next()
    system = OrderingSystem()
    order = system.create_order(ID)

    drink = {}
    print("adding 2 cokain")
    drink[inv.get_ingredient('cokain').name] = 2
    # what kind of burger joint serves sake
    print("adding sake")
    drink[inv.get_ingredient('sake').name] = 1
    system.add_to_order(ID, drink, inv)
    print("printing out order after adding drink")
    order.print_order(inv)
    drink_ingredient = order.drinks.ingredients
    assert drink_ingredient['Sake'] == 1
    assert drink_ingredient['Cokain'] == 2
    assert(order.calculate_order_price(inv) == 207)

def test_addto_drink(gourmet_fixture):
    print("\n ~~~~~~~ test addto drink order ~~~~~~~~~~~~~")
    inv = gourmet_fixture
    IDgen = IdGenerator(0)
    ID = IDgen.next()
    system = OrderingSystem()
    order = system.create_order(ID)

    drink = {}
    print("adding 2 cokain")
    drink[inv.get_ingredient('cokain').name] = 2
    # what kind of burger joint serves sake
    print("adding sake")
    drink[inv.get_ingredient('sake').name] = 1
    system.add_to_order(ID, drink, inv)
    print("printing out order after adding drink\n")
    order.print_order(inv)

    print("adding another 2 cokain")
    drink = {}
    drink[inv.get_ingredient('cokain').name] = 2
    # what kind of burger joint serves sake
    system.add_to_order(ID, drink, inv)
    print("printing out order after adding 2nd batch of drinks\n")
    order.print_order(inv)
    # testing the list of ingredients in drinks
    drink_ingredient = order.drinks.ingredients
    assert drink_ingredient['Sake'] == 1
    assert drink_ingredient['Cokain'] == 4
    assert(order.calculate_order_price(inv) == 345)

def test_id_not_in_sys(gourmet_fixture, order_fixture):
    print("\n ~~~~~~~ test id not in system ~~~~~~~~~~~~~")
    inv = gourmet_fixture
    system = order_fixture

    drink = {}
    drink[inv.get_ingredient('Cokain').name] = 3

    print("trying to add drinks to order number 36")
    with pytest.raises(OrderError) as e:
        system.add_to_order(36, drink, inv)
    assert str(e.value) == 'ID: 36 does not exist, please specify a valid ID.\n'

def test_item_not_in_inv(gourmet_fixture):
    print("\n ~~~~~~~ test items not in system ~~~~~~~~~~~~~")
    inv = gourmet_fixture
    IDgen = IdGenerator(0)
    ID = IDgen.next()
    system = OrderingSystem()
    system.create_order(ID)

    drink = {}
    print("I wanna order a yeet")
    drink["yeet"] = 1
    print("I wanna order a xd")
    drink["xd"] = 1

    print("adding above to order number 1")
    with pytest.raises(OrderError) as e:
        system.add_to_order(ID, drink, inv)
    assert str(e.value) == "We do not serve 'yeet', please specify a valid item.\nWe do not serve 'xd', please specify a valid item.\n"

def test_exceed_max_patty(gourmet_fixture):
    print("\n ~~~~~~~ test exceed max ~~~~~~~~~~~~~")
    inv = gourmet_fixture
    IDgen = IdGenerator(0)
    ID = IDgen.next()
    system = OrderingSystem()
    system.create_order(ID)

    main = {}

    print("adding wrap")
    main[inv.get_ingredient('wrap').name] = 1
    print("I want 5 beef patty in my burger")
    main[inv.get_ingredient('beef patty').name] = 5 

    with pytest.raises(OrderError) as e:
        system.add_to_order(ID, main, inv)
    assert str(e.value) == 'Maximum ordering limit for patty is 3.\n'

def test_exceed_max_different_patty(gourmet_fixture):
    print("\n ~~~~~~~ test exceed max ~~~~~~~~~~~~~")
    inv = gourmet_fixture
    IDgen = IdGenerator(0)
    ID = IDgen.next()
    system = OrderingSystem()
    system.create_order(ID)

    main = {}

    print("adding wrap")
    main[inv.get_ingredient('wrap').name] = 1
    print("I want 2 beef patty and 2 vegetarian patty in my burger")
    main[inv.get_ingredient('beef patty').name] = 2
    main[inv.get_ingredient('vegetarian patty').name] = 2 

    with pytest.raises(OrderError) as e:
        system.add_to_order(ID, main, inv)
    assert str(e.value) == 'Maximum ordering limit for patty is 3.\n'

def test_exceed_max_different_bun(gourmet_fixture):
    print("\n ~~~~~~~ test exceed max ~~~~~~~~~~~~~")
    inv = gourmet_fixture
    IDgen = IdGenerator(0)
    ID = IDgen.next()
    system = OrderingSystem()
    system.create_order(ID)

    main = {}
    main[inv.get_ingredient('Sesame bun').name] = 2
    main[inv.get_ingredient('Mad bun').name] = 3

    with pytest.raises(OrderError) as e:
        system.add_to_order(ID, main, inv)
    assert str(e.value) == 'Maximum ordering limit for bun is 4.\n'

def test_exceed_inventory(gourmet_fixture):
    print("\n ~~~~~~~ test exceed inventory ~~~~~~~~~~~~~")
    inv = gourmet_fixture
    IDgen = IdGenerator(0)
    ID = IDgen.next()
    system = OrderingSystem()
    system.create_order(ID)

    side = {}
    print("I want 200 fries cause imma fatty")
    # there is only 101 fries in inventory
    side[inv.get_ingredient('large fries').name] = 200
    with pytest.raises(OrderError) as e:
        system.add_to_order(ID, side, inv)
    assert str(e.value) == 'Order exceeds inventory: Only 101 of Large fries left in inventory.\n'

def test_less_than_min(gourmet_fixture):
    inv = gourmet_fixture
    IDgen = IdGenerator(0)
    ID = IDgen.next()
    system = OrderingSystem()
    system.create_order(ID)

    main = {}
    main[inv.get_ingredient('sesame bun').name] = 1

    with pytest.raises(OrderError) as e:
        system.add_to_order(ID, main, inv)
    assert str(e.value) == 'Minimum ordering limit for bun is 2.\n'

def test_empty_order(gourmet_fixture):
    inv = gourmet_fixture
    IDgen = IdGenerator(0)
    ID = IDgen.next()
    system = OrderingSystem()
    system.create_order(ID)

    main = {}

    order = system.add_to_order(ID, main, inv)
    assert order == None

# Test Browse Menu
def test_browse(gourmet_fixture):
    print("\n=== Test Browse Menu ===")
    gourmet_fixture.browse_menu()
    assert len(gourmet_fixture.food_list) == 26


# Test Search
def test_search_bun(order_fixture, gourmet_fixture):
    print("\n~~~~~~~~~~~~~~~~ searching for bun ingredient ~~~~~~~~~~~~~~~")
    system = order_fixture
    inv = gourmet_fixture
    search = system.keyword_ingredient_search("bun", "main", inv)
    for item in search:
        print(item)
    assert(len(search) == 4)


def test_search_patty(order_fixture, gourmet_fixture):
    print("\n~~~~~~~~~~~~~~~~ searching for bun ingredient ~~~~~~~~~~~~~~~")
    system = order_fixture
    inv = gourmet_fixture
    search = system.keyword_ingredient_search("patty", "main", inv)
    for item in search:
        print(item)
    assert(len(search) == 3)

def test_search_mains_ingredient(order_fixture, gourmet_fixture):
    print("\n~~~~~~~~~~~~~~~~ searching for mains ingredient ~~~~~~~~~~~~~~~")
    system = order_fixture
    inv = gourmet_fixture
    search = system.keyword_ingredient_search("tom", "main", inv)
    for item in search:
        print(item)
    assert(len(search) == 2)

def test_search_not_in_list(order_fixture, gourmet_fixture):
    print("\n~~~~~~~~~~~~~~~~ searching for patty ingredient ~~~~~~~~~~~~~~~")
    system = order_fixture
    inv = gourmet_fixture
    search = system.keyword_ingredient_search("qweqweqweqw", "main", inv)
    print(search)
    assert(search == 'No results found, Please try again')