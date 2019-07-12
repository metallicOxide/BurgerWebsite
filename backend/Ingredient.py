from abc import ABC

class Ingredient(ABC):

    def __init__(self, name, price, max_allow, quant_type, ingredient_size):
        self._name = name
        self._price = price
        self._max_allow = max_allow
        self._quant_type = quant_type
        self._ingredient_size = ingredient_size

    ''' Properties'''
    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def max_allow(self):
        return self._max_allow

    @property
    def quant_type(self):
        return self._quant_type

    @property
    def ingredient_size(self):
        return self._ingredient_size

    def __str__(self):
        return f'Ingredient: <{self.name}>, <Price: {self.price}>, <Max: {self.max_allow}>, <{self.quant_type}>'

class Bun(Ingredient):
    def __init__(self, name, price, ingredient_size):
        super().__init__(name + ' bun', price, 4, "", ingredient_size)
        #I'm not sure we need a classification
        self._classification = 'bun'
        self._min_allow = 2

    @property
    def classification(self):
        return self._classification

    @property
    def min_allow(self):
        return self._min_allow

class Patty(Ingredient):
    def __init__(self, name, price, ingredient_size):
        super().__init__(name + ' patty', price, 3, "", ingredient_size)
        self._classification = 'patty'

    @property
    def classification(self):
        return self._classification

class MainsIngredient(Ingredient):
    def __init__(self, name, price, max_allow, quant_type, ingredient_size):
        super().__init__(name, price, max_allow, quant_type, ingredient_size)
        self._classification = 'main'

    @property
    def classification(self):
        return self._classification


class Side(Ingredient):
    def __init__(self, name, price, max_allow, quant_type, ingredient_size):
        super().__init__(name, price, max_allow, quant_type, ingredient_size)
        self._classification = 'side'

    @property
    def classification(self):
        return self._classification


class Drink(Ingredient):
    def __init__(self, name, price, max_allow, quant_type, ingredient_size):
        super().__init__(name, price, max_allow, quant_type, ingredient_size)
        self._classification = 'drink'

    @property
    def classification(self):
        return self._classification
