# Ask for the total price of the bill, then ask how 
# many diners there are. Divide the total bill by the 
# number of diners and show how much each 
# person must pay. 

total_bill=int(input("enter total bill amount ? "))
diners=int(input("enter numbers of diners? "))
each_person_share=total_bill / diners
print(f"Each person has to pay {each_person_share}")