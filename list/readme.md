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

#Example 2 :
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
