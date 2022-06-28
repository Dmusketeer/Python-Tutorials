# Sets

- A Python set is an unordered list of immutable elements. It means:
    - Elements in a set are unordered.
    - Elements in a set are unique. A set doesn’t allow duplicate elements.
    - Elements in a set cannot be changed. For example, they can be numbers, strings, and tuples, but cannot be lists or dictionaries.
- To define a set in Python, you use the curly brace {} .


- To define an empty set, you cannot use the curly braces like this:

        empty_set = {}
…because it defines an empty dictionary.

- Therefore, you need to use the built-in set() function:

        empty_set  = set()


- An empty set evaluates to False in Boolean context

- In fact, you can pass an iterable to the set() function to create a set. For example, you can pass a list, which is an iterable, to the set() function like this:
```py
skills = set(['Problem solving','Critical Thinking'])
print(skills)
# Output:
{'Critical Thinking', 'Problem solving'}
```

**Note** that the original order of elements may not be preserved.

- If an iterable has duplicate elements, the set() function will remove them.

```py
characters = set('letter')
print(characters)

# Output:
{'r', 'l', 't', 'e'}
```

## Getting sizes of a set
- To get the number of elements in a set, you use the built-in len() function.

        len(set)

```py
ratings = {10, 20, 30, 40, 50}
size = len(ratings)
print(size)    
# Output:
5
```
## Checking if an element is in a set
- To check if a set contains an element, you use the in operator:

        element in set

- The in operator returns True if the set contains the element.

```py
ratings = {1, 2, 3, 4, 5}
rating = 1

if rating in ratings:
    print(f'The set contains {rating}')

# Output:
The set contains 1
```

## Adding elements to a set

- To add an element to a set, you use the add() method:

        set.add(element)

```py
skills = {'Python programming', 'Software design'}
skills.add('Problem solving')
print(skills)
# Output:
{'Problem solving', 'Software design', 'Python programming'}
```

## Removing an element from a set
- To remove an element from a set, you use the remove() method:

        set.remove(element)
For example:
```py
skills = {'Problem solving', 'Software design', 'Python programming'}
skills.remove('Software design')

print(skills)
# Output:
{'Problem solving', 'Python programming'}
```

## Removing all elements from a set
To remove all elements from a set, you use the clear() method:

set.clear()
Code language: JavaScript (javascript)
For example:
```py
skills = {'Problem solving', 'Software design', 'Python programming'}
skills.clear()
print(skills)
# Output:
set()
```

## Frozen a set
- To make a set immutable, you use the built-in function called frozenset(). The frozenset() returns a new immutable set from an existing one. For example:

```py
skills = {'Problem solving', 'Software design', 'Python programming'}
skills = frozenset(skills)
```
- After that, if you attempt to modify elements of the set, you’ll get an error:

        skills.add('Django')
Error:
        
        AttributeError: 'frozenset' object has no attribute 'add'





