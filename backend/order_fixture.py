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
        inventory.add_stock_type(bun, "bun", 0.69, 10, 4, "discrete")
    # Add wrap
    inventory.add_stock_type("Wrap", "main", 6.69, 10, float("inf"), "discrete")
    # Add patties
    for patty in ["Chicken", "Vegetarian", "Beef"]:
        inventory.add_stock_type(patty, "patty", 6.66, 10, 3, "discrete")
    # Add other main _ingredients
    for misc in ["Tomato", "Lettuce", "Tomato sauce", "Cheddar cheese", "Swiss Cheese"]:
        inventory.add_stock_type(misc, "main", 0.66, 10, float("inf"), "discrete")
    # Add sides
    for side in ["6 pack nuggets", "3 pack nuggets", "Small fries", "Medium fries", "Large fries", "Wiked wingz"]:
        inventory.add_stock_type(side, "side", 4.20, 10, float("inf"), "g")
    # Add _drinks
    for drink in ["Cokain", "Mtn Dew", "Vodka", "Baijiu", "Sake", "Whiskey"]:
        inventory.add_stock_type(drink, "drink", 69, 10, float("inf"), "ml")

    return inventory

@pytest.fixture
def order_fixture(gourmet_fixture):
    inv = gourmet_fixture
    system = OrderingSystem()

    main = []
    main.append(inv.get_ingredient('sesame bun').name)
    main.append(inv.get_ingredient('sesame bun').name)
    main.append(inv.get_ingredient('chicken patty').name)
    main.append(inv.get_ingredient('tomato').name)
    main.append(inv.get_ingredient('Cheddar cheese').name)

    side = []
    side.append(inv.get_ingredient('6 pack nuggets').name)
    side.append(inv.get_ingredient('small fries').name)
    side.append(inv.get_ingredient('small fries').name)

    system.checkout(main, side, None, inv)

    main = []
    main.append(inv.get_ingredient('wrap').name)
    main.append(inv.get_ingredient('vegetarian patty').name)
    main.append(inv.get_ingredient('tomato sauce').name)
    main.append(inv.get_ingredient('lettuce').name)
    main.append(inv.get_ingredient('tomato').name)

    drink = []
    drink.append(inv.get_ingredient('vodka').name)

    system.checkout(main, None, drink, inv)

    main = []
    main.append(inv.get_ingredient('burnt bun').name)
    main.append(inv.get_ingredient('burnt bun').name)
    main.append(inv.get_ingredient('burnt bun').name)
    main.append(inv.get_ingredient('burnt bun').name)
    main.append(inv.get_ingredient('burnt bun').name)
    main.append(inv.get_ingredient('burnt bun').name)
    main.append(inv.get_ingredient('tomato sauce').name)
    main.append(inv.get_ingredient('tomato sauce').name)
    main.append(inv.get_ingredient('tomato sauce').name)
    main.append(inv.get_ingredient('tomato sauce').name)
    main.append(inv.get_ingredient('tomato sauce').name)
    # print("YES I WANT TO END MYSELFFFFFFFFFFF REEEEET but i still want ketchup")
    system.checkout(main, None, None, inv)

    main = []
    main.append(inv.get_ingredient('muffin bun').name)
    main.append(inv.get_ingredient('muffin bun').name)
    main.append(inv.get_ingredient('muffin bun').name)
    main.append(inv.get_ingredient('Vegetarian patty').name)
    main.append(inv.get_ingredient('beef patty').name)
    main.append(inv.get_ingredient('tomato sauce').name)
    main.append(inv.get_ingredient('tomato').name)

    side = []
    side.append(inv.get_ingredient('6 pack nuggets').name)
    side.append(inv.get_ingredient('large fries').name)
    side.append(inv.get_ingredient('wiked wingz').name)

    drink = []
    drink.append(inv.get_ingredient('Mtn dew').name)
    drink.append(inv.get_ingredient('baijiu').name)
    drink.append(inv.get_ingredient('whiskey').name)

    system.checkout(main, side, drink, inv)
    return system

def test_keyword_search(order_fixture, gourmet_fixture):
    system = order_fixture
    inv = gourmet_fixture
    search = system.keyword_ingredient_search("nugget", "side", inv)
    for item in search:
        print(item)
