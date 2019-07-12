from backend.Ordering_system import OrderingSystem
from backend.Ingredient import Bun, Patty, MainsIngredient, Side, Drink
from backend.Order import Order
from backend.Inventory import Inventory
from backend.order_interface import DrinkOrder, SideOrder, MainOrder, Burger, Wrap

import pytest


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
