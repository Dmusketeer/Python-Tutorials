#                       Generators


"""
A Generator object is an iterator, whose values are created at the time of accessing them.

A generator can be obtained either from a generator expression or a generator function.

"""

x = [6, 3, 1]
g = (i**2 for i in x) # generator expression
print(next(g)) # -> 36
print(next(g)) # -> 9

def gen_number():  # generator function
    x = [6, 3, 1]
    for i in x:
        yield i**2
x = gen_number()
next(x)            # -> 36

print(sorted({ ord(i) for i in 'apple' }))
print({0 if i%2 ==0 else 1 for i in range(8)})