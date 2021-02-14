""" Pickling and De_pickling iris data"""
import requests
import pickle

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
rq = requests.get(url).text

lst = [item.split(",") for item in rq.split("\n") if item != '']

# Pickling a python object
with open("iris.pkl", 'wb') as f:
    pickle.dump(lst, f)

# De-Pickling aa python object
with open("iris.pkl", 'rb') as f:
    data = pickle.load(f)
    print(data)
