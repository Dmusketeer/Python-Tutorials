# importing required modeules
import random
import string

print("                                     Password Generator                " )
print("                                   ======================                     ")
numOfPassword=int(input("Number of Password ? "))
passwordLength=int(input("Password Length ? "))
# string.ascii_letters

lower_case=string.ascii_lowercase
upper_case=string.ascii_uppercase
digits=string.digits
special_char=string.punctuation
all_char=lower_case+upper_case+digits+special_char
# print(all_char)
for i in range(numOfPassword):
    temp=random.sample(all_char,passwordLength)
    password="".join(temp)
    print(password)



