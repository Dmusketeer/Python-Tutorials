num=[1,2,3]
# dir() returns list of the attributes and methods of any object
# print(dir(num))#contain __iter__ method not __next__

# for number in num:
#     print(number)   #1,2,3

# NOTE : iterables are not iterator while iterators are iterables

# nums=num.__iter__()
# or
nums=iter(num)
# print(dir(nums)) #  will contain __iter__ & __next__ both


# internal working of for loop

# print(next(nums))#1
# print(next(nums))#2
# print(next(nums))#3

while True:
    try:
        item=next(nums)
        print(item)
    except StopIteration:
        break

# 1 2 3 
