from backend.Inventory import Inventory
from flask import Flask
import pickle

# declaraction that creates flask object assigned to app
# app variable will allow the creation of the structure
app = Flask(__name__)
app.secret_key = 'super-secret-key'  # Used to add entropy

# load the databases from pickle
f = open("stock.pickle", "rb")
inventory = pickle.load(f)
