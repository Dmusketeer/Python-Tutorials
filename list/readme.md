# List

- A list is an ordered collection of items.
- Use square bracket notation [] to access a list element by its index. The first element has an index 0.
- Use a negative index to access a list element from the end of a list. The last element has an index -1.
- Use list[index] = new_value to modify an element from a list.
- Use append() to add a new element to the end of a list.
- Use insert() to add a new element at a position in a list.
- Use pop() to remove an element from a list and return that element.
- Use remove() to remove an element from a list.


# Python Tuples

- Sometimes, you want to create a list of items that cannot be changed throughout the program. Tuples allow you to do that.
- Tuples are immutable lists.
- Use tuples when you want to define a list that cannot change.

## Python Sort List
- Use the Python List sort() method to sort a list in place.
- The sort() method sorts the string elements in alphabetical order and sorts the numeric elements from smallest to largest.
- Use the sort(reverse=True) to reverse the default sort order.

```python
# Example 1 :
    scores = [5, 7, 4, 6, 9, 8]
    scores.sort()
    print(scores)

#o/p : [4, 5, 6, 7, 8, 9]

# Example 2 :
    scores = [5, 7, 4, 6, 9, 8]
    scores.sort(reverse=True)
    print(scores)

#o/p : [9, 8, 7, 6, 5, 4]

```


## Python sorted

- The sort() method sorts a list in place. In other words, it changes the order of elements in the original list.

- To return the new sorted list from the original list, you use the **sorted() function**

```py
    sorted(list)
```

- The sorted() function doesn’t modify the original list.


- Use the sorted() function to return a new sorted list from a list.
- Use the sorted() function with the reverse argument sets to True to sort a list in the reverse sort order.


## Python List Slice

- Lists support the slice notation that allows you to get a sublist from a list:

        sub_list = list[begin: end: step]


## Unpack a List in Python
```py

    colors = ['red', 'blue', 'green']

# To assign the first, second, and third elements of the list to variables, you may assign individual elements to variables like this:

    red = colors[0]
    blue = colors[1]
    green = colors[2]
# However, Python provides a better way to do this. It’s called sequence unpacking.

# Basically, you can assign elements of a list (and also a tuple) to multiple variables. For example:

    red, blue, green = colors

```

- If you use a fewer number of variables on the left side, you’ll get an error. For example:

        colors = ['red', 'blue', 'green']
        red, blue = colors
Error:
ValueError: too many values to unpack (expected 2)

- In this case, Python could not unpack three elements to two variables.

- Unpacking assigns elements of the list to multiple variables.
- Use the asterisk (*) in front of a variable like this *variable_name to pack the leftover elements of a list into another list.

```py

colors = ['cyan', 'magenta', 'yellow', 'black']
cyan, magenta, *other = colors

print(cyan)
print(magenta)
print(other)

# OutPut:
cyan
magenta
['yellow', 'black']

```

## Use a For Loop to Iterate over a List

- Use a for loop to iterate over a list.
- Use a for loop with the enumerate() function to access indexes.

```py
cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']

for city in cities:
    print(city)

# Output:

    New York
    Beijing
    Cairo
    Mumbai
    Mexico

# the for loop assigns an individual element of the cities list to the city variable and prints out the city in each iteration.

```

- Sometimes, you may want to access indexes of elements inside the loop. In these cases, you can use the **enumerate()** function.

- The ***enumerate()*** function returns a tuple that contains the current index and element of the list.


```py

cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']

for item in enumerate(cities):
    print(item)

# Output:
(0, 'New York')
(1, 'Beijing')
(2, 'Cairo')
(3, 'Mumbai')
(4, 'Mexico')

```

- To access the index, you can unpack the tuple within the for loop statement like this:

```py
cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']

for index, city in enumerate(cities):
    print(f"{index}: {city}")


# Output:

0: New York
1: Beijing
2: Cairo
3: Mumbai
4: Mexico

```

- The enumerate() function allows you to specify the starting index which defaults to zero.

- The following example uses the enumerate() function with the index that starts from one:

```py
cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']

for index, city in enumerate(cities,1):
    print(f"{index}: {city}")

# Output:
1: New York
2: Beijing
3: Cairo
4: Mumbai
5: Mexico

```


## Find the Index of an Element in a List

- To find the index of an element in a list, you use the index() function.
```py

cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']

result = cities.index('Mumbai')
print(result)

```
- It returns 3 as expected.

- However, if you attempt to find an element that doesn’t exist in the list using the index() function, you’ll get an error.

