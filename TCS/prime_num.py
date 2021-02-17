num=int(input('enter the number to be checked for prime :'))
count=2
while count < num:
    if num%count==0:
        print('number is not prime')
        break
    count+=1
else:
    print('number is prime')
