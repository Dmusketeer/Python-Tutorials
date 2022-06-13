# The Python ternary operator is ``value_if_true if condition else value_if_false.``
# Use the ternary operator to make your code more concise.

age = input('Enter your age:')
ticket_price = 20 if int(age) >= 18 else 5
print(f"The ticket price is {ticket_price}")