import sys
import keyword
print(keyword.kwlist)

print(len(keyword.kwlist))


def sum(a, b):
    return a+b


print(sum(2, 3))

print("==========================")


val1 = 10
print(sys.getsizeof(val1))
