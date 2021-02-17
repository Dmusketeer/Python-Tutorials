Oddly Even Problem Statement
Given a maximum of 100 digit numbers as input, find the difference between the sum of odd and even position digits

Test Cases
Case 1
Input: 4567
Expected Output: 2


Solution:
num = [int(d) for d in str(input("Enter the number:"))]
even,odd = 0,0
for i in range(0,len(num)):
    if i % 2 ==0:
        even = even + num[i]
    else:
        odd = odd + num[i]
print(abs(odd-even))
