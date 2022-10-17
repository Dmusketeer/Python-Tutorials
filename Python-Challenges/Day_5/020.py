# Ask the user to enter their first name and surname in lower 
# case. Change the case to title case and join them together. 
# Display the finished result.

fname=input("Enter first name in lower case: ")
fnameT=fname.title()
sname=input("Enter surname in lower case: ")
snameT=sname.title()
print(f"{fnameT} {snameT}")