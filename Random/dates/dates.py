# date in python in not a data type
import datetime
from time import strftime


# return year, month, day, hours, minutes, second, Microsecond.
# print(datetime.datetime.now())
# print(datetime.datetime.now().year)
# print(datetime.datetime.now().month)
# print(datetime.datetime.now().day)


# To create a date, we can use the datetime() class (constructor) of the datetime module.
# The datetime() class requires three parameters to create a date: year, month, day.
# The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), 
# but they are optional, and has a default value of 0, (None for timezone).
x=datetime.datetime(2022,4,23)

# The strftime() Method
# The datetime object has a method for formatting date objects into readable strings.
# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:

print(strftime("%Y-%m-%d"))
print(strftime("%B"))
print(strftime("%A"))
print(strftime("%j"))#Day number
print(strftime("%X"))
print(x)