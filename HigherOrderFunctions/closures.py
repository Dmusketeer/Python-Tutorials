"""
                                            Closures

In simplest terms, a Closure is a function returned by a higher order function, whose return value depends on the data associated with the higher order function.


"""
# Example
def multiple_of(x):
    def multiple(y):
        return x*y
    return multiple
c1 = multiple_of(5)  # 'c1' is a closure
c2 = multiple_of(6)  # 'c2' is a closure
print(c1(4)) #20
print(c2(4)) #24

"""
You can observe from the example that the closure functions c1 and c2 hold the data passed to enclosing function, multiple_of, during their creation.

The first closure function, c1 binds the value 5 to argument x and when called with an argument 4, it executes the body of multiple function and returns the product of 5 and 4.

Similarly c2 binds the value 6 to argument x and when called with argument 4 returns 24.
"""



