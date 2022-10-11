# Ask the user to enter three 
# numbers. Add together the first 
# two numbers and then multiply 
# this total by the third. Display the 
# answer as The answer is 
# [answer].

num1,num2,num3=map(int,input('Enter three numbers :').split())
print(f"The Answer is {(num1+num2)*num3}")