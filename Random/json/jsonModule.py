# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.
# Python has a built-in package called json, which can be used to work with JSON data.

# import module
import json

# convert from json to Python
# If you have a JSON string, you can parse it by using the json.loads() method.

# some json
details =  '{ "name":"Dheeraj", "age":26, "city":"Pune"}'
list_o='["name","Dheeraj", "age",26, "city","Pune"]'
# parse x:
y = json.loads(details)
z = json.loads(list_o)

print(y)

print(type(y)) #Python dictionary
print(type(z)) #python list

print("===========================")

# Convert from Python to JSON
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

py_dict=y
c_json=json.dumps(py_dict)
print(c_json)
print(type(c_json)) # type str



# You can convert Python objects of the following types, into JSON strings:

# dict
# list
# tuple
# string
# int
# float
# True
# False
# None

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))






xx = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# convert into JSON:
yy = json.dumps(xx)

# the result is a JSON string:
print(yy)
