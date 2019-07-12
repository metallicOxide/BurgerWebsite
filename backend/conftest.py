from backend.Ordering_system import OrderingSystem
from backend.Ingredient import Bun, Patty, MainsIngredient, Side, Drink
from backend.Order import Order
from backend.Inventory import Inventory
from backend.order_interface import DrinkOrder, SideOrder, MainOrder, Burger, Wrap

import pytest

@pytest.fixture
def gourmet_fixture():
    # How would I make different stuff have different prices
    inventory = Inventory()
    # Add buns
    for bun in ["Sesame", "Muffin", "Mad", "Burnt"]:
        inventory.add_stock_type(bun, "bun", 0.69, 10, 1, 4, "discrete")
    # Add wrap
    inventory.add_stock_type("Wrap", "main", 6.69, 12, 1, float("inf"), "discrete")
    # Add patties
    for patty in ["Chicken", "Vegetarian", "Beef"]:
        inventory.add_stock_type(patty, "patty", 6.66, 20, 1, 3, "discrete")
    # Add other main _ingredients
    inventory.add_stock_type("Base", "main", 5.50, 50, 1, float("inf"), "discrete")
    for misc in ["Tomato", "Lettuce", "Tomato sauce", "Cheddar cheese", "Swiss Cheese"]:
        inventory.add_stock_type(misc, "main", 0.66, 69, 1, float("inf"), "discrete")
    # Add sides
    for side in ["6 pack nuggets", "3 pack nuggets", "Small fries", "Medium fries", "Large fries", "Wiked wingz"]:
        inventory.add_stock_type(side, "side", 4.20, 101, 3, float("inf"), "g")
    # Add _drinks
    for drink in ["Cokain", "Mtn Dew", "Vodka", "Baijiu", "Sake", "Whiskey"]:
        inventory.add_stock_type(drink, "drink", 69, 11, 1, float("inf"), "ml")

    return inventory

@pytest.fixture
def order_fixture(gourmet_fixture):
    inv = gourmet_fixture
    system = OrderingSystem()

    # ORDER 1
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

    # ORDER 2
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

    # ORDER 3
    main = {}
    main[inv.get_ingredient('burnt bun').name] = 4
    main[inv.get_ingredient('tomato sauce').name] = 5 

    mains = []
    mains.append(main)
    system.checkout(mains, None, None, inv)

    # ORDER 4
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

    # ORDER 5
    main = {}
    main[inv.get_ingredient('mad bun').name] = 2
    main[inv.get_ingredient('Vegetarian patty').name] = 1 
    main[inv.get_ingredient('beef patty').name] = 1
    main[inv.get_ingredient('tomato sauce').name] = 1
    main[inv.get_ingredient('tomato').name] = 1

    side = {}
    side[inv.get_ingredient('6 pack nuggets').name] = 1
    side[inv.get_ingredient('large fries').name] = 1 

    drink = {}
    drink[inv.get_ingredient('Mtn dew').name] = 1

    mains = []
    mains.append(main)
    system.checkout(mains, side, drink, inv)

    return system
