# Write a program that will ask for a 
# number of days and then will show how many hours, minutes and seconds are in that number of days. 
days=int(input("Enter numbers of days : "))
hours =days*24
minutes=hours*60
second=minutes*60
print(f"There are {hours} hours, {minutes} minutes, {second} second in {days} days")