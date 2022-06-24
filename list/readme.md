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

```py
cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']

result = cities.index('Osaka')
print(result)

Error:
ValueError: 'Osaka' is not in list

```


- Use the in operator with the index() function to find if an element is in a list.


## Python Iterables

- In Python, an iterable is an object that includes zero, one, or many elements. An iterable has the ability to return its elements one at a time.

- Because of this feature, you can use a for loop to iterate over an iterable.

- In fact, the range() function is an iterable because you can iterate over its result:

```py
for index in range(3):
    print(index)

# Output:
0
1
2

```

- The rule of thumb is that if you know if can loop over something, it’s iterable.

## What is an iterator
- An iterable can be iterated over. And an iterator is the agent that performs the iteration.

- To get an iterator from an iterable, you use the **iter()** function. For example:
```py
colors = ['red', 'green', 'blue']
colors_iter = iter(colors)
```
once you have the iterator, you can get the next element from the iterable using the next() function:

```py
colors = ['red', 'green', 'blue']
colors_iter = iter(colors)

color = next(colors_iter)
print(color)

color = next(colors_iter)
print(color)

color = next(colors_iter)
print(color)

# Output:
red
green
blue

```

- If there isn’t any more element and you call the next() function, you’ll get an exception.

- The iterator is stateful. It means that once you consume an element from the iterator, it’s gone.

- In other words, once you complete looping over an iterator, the iterator becomes empty. If you iterate over it again, it’ll return nothing.

- Since you can iterate over an iterator, the iterator is also an iterable object. 


## Map() Function

When working with a list (or a tuple), you often need to transform the elements of the list and return a new list that contains the transformed element.

```py
# double the each elements
lst=[10,20,30,40]
lst1=[]
for i in lst:
    lst1.append(i*2)

# Output : [20,40,60,80]

```

- Python provides a nicer way to do this kind of task by using the **map()** built-in function.
- Python provides a nicer way to do this kind of task by using the map() built-in function.

- Syntax of map() function:
        
        iterator = map(fn, list)


- In this syntax, fn is the name of the function that will call on each element of the list.

- In fact, you can pass any **iterable** to the **map()** function, not just a list or tuple.


```py

# double each elements in list
lst=[10,20,30,40,50]
def double(ele):
    return ele*2
itr=map(double,lst) #it will return iterator 
print(list(itr))

# make this code more concise by using a lambda expression like this:

lst=[10,20,30,40,50]

itr=map(lambda ele:ele*2,lst)
print(list(itr)) # convert into iterable

```

## filter() function
## How to Filter List Elements in Python

- Sometimes, you need to iterate over elements of a list and select some of them based on specified criteria.

- Use the Python filter() function to filter a list (or a tuple).
```py
lst=[10,20,30,40,50]
lst1=[]
for i in lst:
    if i > 30:
        lst1.append(i)

print(lst1)
``` 

- Python has a built-in function called filter() that allows you to filter a list (or a tuple) in a more beautiful way.

        filter(fn, list)


- The filter() function iterates over the elements of the list and applies the fn() function to each element. It returns an iterator for the elements where the fn() returns **True**.

- In fact, you can pass any iterable to the second argument of the filter() function, not just a list.


```py
lst=[10,20,30,40,50]
filtered=filter(lambda ele:ele>20,lst)
print(list(filtered))
``` 
- Since the filter() function returns an iterator, you can use a for loop to iterate over it. Or you can use the list() function to convert the iterator to a list.


Example :

```py
    countries = [
        ['China', 1394015977],
        ['United States', 329877505],
        ['India', 1326093247],
        ['Indonesia', 267026366],
        ['Bangladesh', 162650853],
        ['Pakistan', 233500636],
        ['Nigeria', 214028302],
        ['Brazil', 21171597],
        ['Russia', 141722205],
        ['Mexico', 128649565]
    ]

    # get all the countries whose populations are greater than 300 million using filter function
    filtered=filter(lambda c: c[1]>300000000, countries)
    print(list(filtered))

```


## Reduce() function
### Reducing a list

- Sometimes, you want to reduce a list to a single value. For example, suppose that you have a list of numbers

```py
marks=[50,22,10,70,80]
# sum of all the elements
total=0
for mark in marks:
    total=total+mark
print(total)

# we have reduced the whole list into a single value
```

- Python offers a function called **reduce()** that allows you to reduce a list in a more concise way.

syntax:
        
        reduce(fn,list)



- The reduce() function applies the fn function of two arguments cumulatively to the items of the list, from left to right, to reduce the list into a single value.

- Unlike the map() and filter() functions, the reduce() isn’t a built-in function in Python. In fact, the reduce() function belongs to the functools module.

- To use the reduce() function, you need to import it from the functools module

        from functools import reduce


```py
from functools import reduce
marks=[50,22,10,70,80]
# sum of all the elements
total=reduce(lambda a,b:a+b,marks)
print(total)

```