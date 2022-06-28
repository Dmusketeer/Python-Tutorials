# Python Dictionary type

- A Python dictionary is a collection of key-value pairs where each key is associated with a value.

- A **value** in the key-value pair can be a number, a string, a list, a tuple, or even another dictionary. In fact, you can use a **value** of any valid type in Python as the value in the key-value pair.

- A key in the key-value pair must be immutable.
- Python uses the curly braces {} to define a dictionary. Inside the curly braces, you can place zero, one, or many key-value pairs.

```py
emp_dict={}
```

- To find the type of a dictionary, you use the type() function
```py
    print(type(empty_dict))
    # Ouptut:
    <class 'dict'>
```


### Accessing the value from dictionary

- we can use the bracket notation([]) or get() method to access the value from the dictionary 
```
dict[key]
```

```py
person={
    "fname":"Dheeraj",
    "lname":"Tiwari",
    "age":26,
    "friends":["Prakhar","Dinesh","Rahul"],
    "Intrested":True
}
# bracket nottion to access the element of dict
print(person["fname"])
print(person["friends"])
```

- If you attempt to access a key that doesn’t exist, you’ll get an error

```py
person["Home"]

# KeyError: 'Home'
```

- To avoid this error, you can use the get() method of the dictionary
```py
myfnds=person.get("friends")
```
- If the key doesn’t exist, the get() method returns None instead of throwing a KeyError. Note that None means no value exists.

### Adding new key-value pairs

```py
person['gender'] = 'Male'
```

### Modifying values in a key-value pair

```py
person['age'] = 27
```

### Removing key-value pairs

```py
del dict[key]
```

### Looping through a dictionary

1) Looping all key-value pairs in a dictionary
    - Python dictionary provides a method called items() that returns an object which contains a list of key-value pairs as tuples in a list.


```py
person={
    "fname":"Dheeraj",
    "lname":"Tiwari",
    "age":26,
    "friends":["Prakhar","Dinesh","Rahul"],
    "Intrested":True
}

#output:
dict_items([('fname', 'Dheeraj'), ('lname', 'Tiwari'), ('age', 26), ('friends', ['Prakhar', 'Dinesh', 'Rahul']), ('Intrested', True)])
```

- To iterate over all key-value pairs in a dictionary, you use a for loop with two variable key and value to unpack each tuple of the list


```py
for key,value in person.items():
    print(f"{Key} -> {value}")
```

- **Note** that you can use any variable name in the for loop. They don’t have to be the key and value.

2)
    - Looping through all the keys in a dictionary
    Sometimes, you just want to loop through all keys in a dictionary. In this case, you can use a for loop with the keys() method.

    - The keys() method returns an object that contains a list of keys in the dictionary.


    ```py
    for key in person.keys():
    print(f"{key}")
    ```

    - similarly for the values, The values() method returns a list of values without any keys.
    ```py
    for value in person.values():
    print(f"{value}")
    ```

# Python Dictionary Comprehension

- A dictionary comprehension iterates over items of a dictionary and allows you to create a new dictionary by transforming or filtering each item.
- A dictionary comprehension allows you to run a for loop on a dictionary and do something on each item like transforming or filtering, and returns a new dictionary.

- Unlike a for loop, a dictionary comprehension offers a more expressive and concise syntax when you use it correctly.


**syntax** :
{key:value for (key,value) in dict.items() if condition}

```py
stocks = {
    'AAPL': 121,
    'AMZN': 3380,
    'MSFT': 219,
    'BIIB': 280,
    'QDEL': 266,
    'LVGO': 144
}

# increase the price of each stock by 2%
new_stocks = {}
for symbol, price in stocks.items():
    new_stocks[symbol] = price*1.02
print(new_stocks)

```

- dictionary comprehension to achieve the same result

```py
new_stocks = {symbol: price * 1.02 for (symbol, price) in stocks.items()}
```

### Filter a dictionary:
- select stocks whose prices are greater than 200
```py
selected_stocks = {s: p for (s, p) in stocks.items() if p > 200}
print(selected_stocks)
```
