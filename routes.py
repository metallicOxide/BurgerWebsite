from flask import render_template, request, redirect, url_for, abort, session
from server import app, inventory
from backend.errors import *
from backend.Order import Order
from backend.Ordering_system import OrderingSystem
from backend.helper import merge_dictonaries
import pickle
# import other modules as required

'''
Dedicated page for "page not found"
'''
@app.route('/404')
@app.errorhandler(404)
def page_not_found(e=None):
    return render_template('404.html'), 404 


'''
Set global variable newOrder
'''
newOrder = 0

'''
Home Page
'''
@app.route('/')
def home():
    global newOrder
    print(newOrder)
    if newOrder == 0:
        newOrder = 1
        order = []
        mains = []
        sides = {}
        drinks = {}
        order.append(mains)
        order.append(sides)
        order.append(drinks)
        f = open("temp_order.pickle", "wb")
        pickle.dump(order, f)
        f.close()
    return render_template('home.html')

'''
Mains Page
'''
@app.route('/mains')
def mains():

    return render_template('mains.html')

'''
Premade items
'''
@app.route('/ClassicBurger', methods=["GET", "POST"])
def premade():
    f = open("stock.pickle", "rb")
    inventory = pickle.load(f)
    f.close()

    if request.method == 'POST':
        f = open("temp_order.pickle", "rb")
        order = pickle.load(f)

        premade_ingredients = {}
        for food in inventory.food_list:
            if food.name == 'Classic Burger' and request.form.get(food.name) != '0':
                premade_ingredients[food.name] = int(request.form.get(food.name))
            elif food.name == 'Classic Wrap' and request.form.get(food.name) != '0':
                premade_ingredients[food.name] = int(request.form.get(food.name))

        errors = check_order_error(None, 'temp', premade_ingredients, inventory)
        if len(premade_ingredients) == 0:
            errors["Please add item to cart"] = "Nothing added"

        temp = {}
        for food_dict in order[0]:
            temp = merge_dictonaries(temp, food_dict)
        temp = merge_dictonaries(temp, premade_ingredients)

        for key in temp:
            stock = inventory.get_ingredient(key)
            if temp[key] * stock.ingredient_size > inventory.get_stock_quantity(key):
                errors["Order exceeds inventory: Only {0} of {1} left in inventory".format(inventory.get_stock_quantity(key), key, temp[key] * stock.ingredient_size)] = "item out of stock"
        if errors:
            return render_template('premade.html', error = errors, ingredients = premade_ingredients, list = inventory.food_list)
        else:
            order[0].append(premade_ingredients)
            f = open("temp_order.pickle", "wb")
            pickle.dump(order, f)
            return redirect(url_for('sides'))
    return render_template('premade.html', list = inventory.food_list)


'''
Wraps
'''
@app.route('/Gourmet_Wrap', methods=["GET", "POST"])
def wraps():
    f = open("stock.pickle", "rb")
    inventory = pickle.load(f)
    f.close()

    if request.method == 'POST':
        f = open("temp_order.pickle", "rb")
        order = pickle.load(f)

        wrap_ingredients = {}
        for food in inventory.food_list:
            if (food.classification == 'patty' or food.classification == 'main') and (request.form.get(food.name) != '0' and request.form.get(food.name) != None):
                wrap_ingredients[food.name] = int(request.form.get(food.name))

        errors = check_order_error(None, 'temp', wrap_ingredients, inventory)
        if len(wrap_ingredients) == 0:
            errors["Please add item to cart"] = "Nothing added"    
            
        temp = {}
        for food_dict in order[0]:
            temp = merge_dictonaries(temp, food_dict)
        temp = merge_dictonaries(temp, wrap_ingredients)  

        for key in temp:
            stock = inventory.get_ingredient(key)
            if temp[key] * stock.ingredient_size > inventory.get_stock_quantity(key):
                errors["Order exceeds inventory: Only {0} of {1} left in inventory".format(inventory.get_stock_quantity(key), key, temp[key] * stock.ingredient_size)] = "item out of stock"

        if errors:
            return render_template('wraps.html', error = errors, ingredients = wrap_ingredients, list = inventory.food_list)
        else:
            order[0].append(wrap_ingredients)
            f = open("temp_order.pickle", "wb")
            pickle.dump(order, f)
            return redirect(url_for('sides'))
    return render_template('wraps.html', list = inventory.food_list)


'''
Burgers
'''
@app.route('/Gourmet_burger', methods=["GET", "POST"])
def burgers():
    f = open("stock.pickle", "rb")
    inventory = pickle.load(f)
    f.close()

    if request.method == 'POST':
        f = open("temp_order.pickle", "rb")
        order = pickle.load(f)
        f.close()

        burger_ingredients = {}
        for food in inventory.food_list:
            if (food.classification == 'patty' or food.classification == 'main' or food.classification == 'bun') and (request.form.get(food.name) != '0' and request.form.get(food.name) != None):
                burger_ingredients[food.name] = int(request.form.get(food.name))

        errors = check_order_error(None, 'temp', burger_ingredients, inventory)
        if len(burger_ingredients) == 0:
            errors["Please add item to cart"] = "Nothing added" 
        temp = {}
        for food_dict in order[0]:
            temp = merge_dictonaries(temp, food_dict)
        temp = merge_dictonaries(temp, burger_ingredients)  

        for key in temp:
            stock = inventory.get_ingredient(key)
            if temp[key] * stock.ingredient_size > inventory.get_stock_quantity(key):
                errors["Order exceeds inventory: Only {0} of {1} left in inventory".format(inventory.get_stock_quantity(key), key, temp[key] * stock.ingredient_size)] = "item out of stock"

        if errors:
            return render_template('burgers.html', error = errors, ingredients = burger_ingredients, list = inventory.food_list)
        else:
            order[0].append(burger_ingredients)
            f = open("temp_order.pickle", "wb")
            pickle.dump(order, f)
            return redirect(url_for('sides'))
    return render_template('burgers.html', list = inventory.food_list)


'''
Ingredients Page
'''
@app.route('/ingredients')
def ingredients():
    f = open("stock.pickle", "rb")
    inventory = pickle.load(f)
    buns = []
    patties = []
    wraps = []
    misc = []
    sides = []
    drinks = []
    for food in inventory.food_list:
        if food.classification == 'bun':
            buns.append(food)
        if food.classification == 'patty':
            patties.append(food)
        if 'wrap' in food.name.lower():
            wraps.append(food)
        if food.classification == 'main' and food.name.lower() != 'wrap':
            misc.append(food)
        if food.classification == 'side':
            sides.append(food)
        if food.classification == 'drink':
            drinks.append(food)
    return render_template('ingredients.html', buns=buns, patties=patties, wraps=wraps, misc=misc, sides=sides, drinks=drinks)

'''
Sides Page
'''
@app.route('/sides', methods=["GET", "POST"])
def sides():
    f = open("stock.pickle", "rb")
    inventory = pickle.load(f)
    f.close()

    if request.method == 'POST':
        f = open("temp_order.pickle", "rb")
        order = pickle.load(f)
        f.close()

        side_ingredients = {}
        for food in inventory.food_list:
            if food.classification == 'side' and request.form.get(food.name) != '0':
                side_ingredients[food.name] = int(request.form.get(food.name))

        errors = check_order_error(None, 'temp', side_ingredients, inventory)

        temp = {}
        temp = merge_dictonaries(temp, order[1])
        temp = merge_dictonaries(temp, side_ingredients)  

        for key in temp:
            stock = inventory.get_ingredient(key)
            if temp[key] * stock.ingredient_size > inventory.get_stock_quantity(key):
                errors["Order exceeds inventory: Only {0} of {1} left in inventory".format(inventory.get_stock_quantity(key), key, temp[key] * stock.ingredient_size)] = "item out of stock"
            
        if errors:
            return render_template('sides.html', error = errors, ingredients = side_ingredients, list = inventory.food_list)
        else:
            order[1] = merge_dictonaries(order[1], side_ingredients)
            f = open("temp_order.pickle", "wb")
            pickle.dump(order, f)
            return redirect(url_for('drinks'))
    return render_template('sides.html', list = inventory.food_list)

'''
Drinks Page
'''
@app.route('/drinks', methods=["GET", "POST"])
def drinks():
    f = open("stock.pickle", "rb")
    inventory = pickle.load(f)

    if request.method == 'POST':
        f = open("temp_order.pickle", "rb")
        order = pickle.load(f)
        f.close()

        drink_ingredients = {}
        for food in inventory.food_list:
            if food.classification == 'drink' and request.form.get(food.name) != '0':
                drink_ingredients[food.name] = int(request.form.get(food.name))

        errors = check_order_error(None, 'temp', drink_ingredients, inventory)

        temp = {}
        temp = merge_dictonaries(temp, order[2])
        temp = merge_dictonaries(temp, drink_ingredients)  

        for key in temp:
            stock = inventory.get_ingredient(key)
            if temp[key] * stock.ingredient_size > inventory.get_stock_quantity(key):
                errors["Order exceeds inventory: Only {0} of {1} left in inventory, t".format(inventory.get_stock_quantity(key), key, temp[key] * stock.ingredient_size)] = "item out of stock"

        if errors:
            return render_template('drinks.html', error = errors, ingredients = drink_ingredients, list = inventory.food_list)
        else:
            order[2] = merge_dictonaries(order[2], drink_ingredients)
            f = open("temp_order.pickle", "wb")
            pickle.dump(order, f)
            return redirect(url_for('myCart'))

    return render_template('drinks.html', list = inventory.food_list)

'''
My Cart Page
'''
@app.route('/myCart', methods=["GET", "POST"])
def myCart():
    global newOrder

    if newOrder == 0:
        return redirect(url_for('home'))


    f = open("stock.pickle", "rb")
    inventory = pickle.load(f)
    f.close

    f = open("temp_order.pickle", "rb")
    order = pickle.load(f)
    f.close()

    f = open("system.pickle", "rb")
    try:
        system = pickle.load(f)
    except EOFError:
        f.close()
        system = OrderingSystem()
    finally:
        print(newOrder)
        if request.method == "POST":
            if request.form.get("Cancel Order") != None:
                newOrder = 0
                return redirect(url_for('home'))
            else:
                try:
                    ID = system.checkout(order[0], order[1], order[2], inventory)
                except OrderError as error:
                    return render_template('my_cart.html', order = order, inventory = inventory, error = error)
                else:
                    newOrder = 0
                    f = open("system.pickle", "wb")
                    pickle.dump(system, f)
                    f = open("stock.pickle", "wb")
                    pickle.dump(inventory, f)
                    f.close
                    return redirect(url_for('myOrder', orderID = ID))
        
    # price calculating logic
    price = 0
    total = {}
    for main in order[0]:
        total = merge_dictonaries(total, main)
    total = merge_dictonaries(total, order[1])
    total = merge_dictonaries(total, order[2])
    for key in total:
        stock = inventory.get_ingredient(key)
        price = price + stock.price * total[key]
    
    return render_template('my_cart.html', order = order, inventory = inventory, price = price)

'''
My Order Page
'''
@app.route('/myOrder/<orderID>')
def myOrder(orderID):
    f = open("system.pickle", "rb")
    system = pickle.load(f)

    f = open("stock.pickle", "rb")
    inventory = pickle.load(f)
    f.close

    order = system.get_curr_order_by_ID(int(orderID))
    return render_template('my_order.html', ID = orderID, order = order, inventory = inventory)


'''
Track Order Page
'''
@app.route('/trackOrder', methods=['GET', 'POST'])
def trackOrder():
    # load order pickle file
    order_sys = open("system.pickle", "rb")
    orders = pickle.load(order_sys)
    current_orders = orders.curr_orders
    print(current_orders)

    # load inventory pickle file
    f = open("stock.pickle", "rb")
    inventory = pickle.load(f)
    results = False

    if request.method == "POST":
        # empty search

        if request.form['track_order_search'] == None or request.form['track_order_search'] == "":
            errors = check_id_error(orders, None)
            return render_template('track_order.html', errors=errors)
        else:
            try:
                order_id = int(request.form['track_order_search'])
                print("order_id", order_id)
                errors = check_id_error(orders, order_id)
                if errors:
                    raise TrackOrderError(errors)
            except TrackOrderError as error:
                return render_template('track_order.html', errors=errors)
            else:
                results = orders.get_curr_order_by_ID(order_id)
                return render_template('track_order.html', result=[results], inventory=inventory, errors=errors)

    return render_template('track_order.html')

'''
Current Orders Page
'''
@app.route('/currentOrders', methods=['GET', 'POST'])
def currentOrders():
    errors = []
    # load order pickle file
    order_sys = open("system.pickle", "rb")
    orders = pickle.load(order_sys)
    current_orders = orders.curr_orders

    # load inventory pickle file
    f = open("stock.pickle", "rb")
    inventory = pickle.load(f)

    # setting order status and deletion
    if request.method == 'POST':
        if request.form['update_status'] == 'update':
            order_id = int(request.form['id'])
            print("order_id:", order_id)
            order_set = str(request.form["order_status"])
            if order_id != None:
                orders.set_order_status(order_set, "Current", order_id)
        elif request.form['update_status'] == 'delete':
            order_id = int(request.form['id_del'])
            print("order_id:", order_id)
            if order_id != None:
                orders.clear_orders("Current", order_id)
        elif request.form['update_status'] =='clear':
            orders.clear_orders("Current")
        order_sys=open("system.pickle", "wb")
        pickle.dump(orders, order_sys)
        order_sys.close()

    # search form
    if request.args.get('search_str') is not None and request.args.get('search_str') != "":
        try:
            search_ID = int(request.args['search_str'])
            print("search ID:",search_ID)
            errors = check_id_error(orders,search_ID)
            if errors:
                raise TrackOrderError(errors)
        except TrackOrderError as error:
            return render_template('current_orders.html', curr_orders=current_orders, inventory=inventory, errors=errors)
        else:
            results = orders.get_curr_order_by_ID(search_ID)
            search = True
            return render_template('current_orders.html', curr_orders=[results], inventory=inventory, search = search )
    elif request.args.get('search_str') is None or request.args.get('search_str') == "":
        return render_template('current_orders.html', curr_orders=current_orders, inventory=inventory, errors=errors )

    return render_template('current_orders.html', curr_orders=current_orders, inventory=inventory )
'''
Completed Orders Page
'''
@app.route('/completedOrders', methods=["GET", "POST"])
def completedOrders():
    order_sys = open("system.pickle", "rb")
    orders = pickle.load(order_sys)

    # load inventory pickle file
    f = open("stock.pickle", "rb")
    inventory = pickle.load(f)

    # setting order status and deletion
    if request.method == 'POST':
        if request.form['update_status'] == 'update':
            order_id = int(request.form['id'])
            print("order_id:", order_id)
            order_set = str(request.form["order_status"])
            if order_id != None:
                orders.set_order_status(order_set, "Completed", order_id)
        elif request.form['update_status'] == 'delete':
            order_id = int(request.form['id_del'])
            print("order_id:", order_id)
            if order_id != None:
                orders.clear_orders("Completed", order_id)
        elif request.form['update_status'] == 'clear':
            orders.clear_orders("Completed")
        order_sys=open("system.pickle", "wb")
        pickle.dump(orders, order_sys)
        order_sys.close()

    # search form
    if request.args.get('search_str') is not None and request.args.get('search_str') != "":
        try:
            search_ID = int(request.args['search_str'])
            print("searchID:",int(request.args['search_str']))
            errors = check_comp_order_id_error(orders, search_ID)
            if errors:
                raise TrackOrderError(errors)
        except TrackOrderError as error:
            return render_template('completed_orders.html', comp_orders=orders.completed_orders, inventory=inventory, errors=errors)
        else:
            results = orders.get_completed_order_by_ID(search_ID)
            search = True
            return render_template('completed_orders.html', comp_orders=[results], inventory=inventory, search=search)
    elif request.args.get('search_str') is None or request.args.get('search_str') == "":
        return render_template('completed_orders.html', comp_orders=orders.completed_orders, inventory=inventory)

    return render_template('completed_orders.html', comp_orders=orders.completed_orders, inventory=inventory)


'''
Inventory Page
'''
@app.route('/inventory')
def manage_inventory():
    f = open("stock.pickle", "rb")
    inventory = pickle.load(f)
    return render_template('manage_inventory.html', food_dict=inventory.food_dict, food_list=inventory.food_list)

'''
Ingredient Details Page
'''
@app.route('/inventory/<ingredient_name>', methods=["GET", "POST"])
def ingredient_details(ingredient_name):
    f = open("stock.pickle", "rb")
    inventory = pickle.load(f)
    ingredient = inventory.get_ingredient(ingredient_name)
    quant = inventory.food_dict[ingredient_name]

    if request.method == 'POST':
        if request.form['submit'] == 'update':
            amount = request.form.get('amount')
            if amount != "":
                amount = int(amount)
            error = inventory.update_stock_quantity(ingredient_name, amount)
            f = open("stock.pickle", "wb")
            pickle.dump(inventory, f)
            ingredient = inventory.get_ingredient(ingredient_name)
            quant = inventory.food_dict[ingredient_name]
            if error:
                return render_template('ingredient_details.html', error=error, ingredient=ingredient, quant=quant)
            else:
                return render_template('ingredient_details.html', ingredient=ingredient, quant=quant)
        elif request.form['submit'] == 'remove':
            inventory.delete_stock(ingredient_name)
            f = open("stock.pickle", "wb")
            pickle.dump(inventory, f)
            return redirect(url_for('manage_inventory'))
    return render_template('ingredient_details.html', ingredient=ingredient, quant=quant)
'''
Add new stock type form
'''
@app.route('/inventory/addStock', methods=["GET", "POST"])
def add_stock():
    if request.method == 'POST':
        if request.form['submit'] == 'confirm':
            # Get all form data
            name = request.form.get('name')
            classification = request.form.get('classification')
            price = request.form.get('price')
            if price != "":
                price = float(price)
            amount = request.form.get('amount')
            if amount != "":
                amount = int(amount)
            ingredient_size = request.form.get('ingredient_size')
            if ingredient_size != "":
                ingredient_size = int(ingredient_size)
            max_allow =  request.form.get('max_allow')
            if max_allow == "" or max_allow is None:
                max_allow = float("inf")
            else:
                max_allow = int(max_allow)
            quant_type = request.form.get('quant_type')

            # Add item to inventory
            f = open("stock.pickle", "rb")
            inventory = pickle.load(f)
            errors = inventory.add_stock_type(name, classification, price, amount, ingredient_size, max_allow, quant_type)
            f = open("stock.pickle", "wb")
            pickle.dump(inventory, f)
            if errors:
                if max_allow == float("inf"):
                    max_allow = ""
                return render_template('add_stock.html', errors=errors, name=name, price=price, ingredient_size=ingredient_size, amount=amount, max_allow=max_allow, quant_type=quant_type)
            return redirect(url_for('manage_inventory'))

        elif request.form['submit'] == 'cancel':
            return redirect(url_for('manage_inventory'))

    return render_template('add_stock.html')
