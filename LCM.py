def gcd(a,b): 
  
    # base case if a and b are equal  
    if (a == b): 
        return a 
    # if a is greater 
    if (a > b): 
        return gcd(a-b, b) 
          
    return gcd(a, b-a) 
  
# Function to return LCM of two numbers 
def lcm(a,b): 
    return (a*b) / gcd(a,b) 
  
# Driver program to test above function 
a,b=map(int,input().split(' ')) 
print('LCM of', a, 'and', b, 'is', lcm(a, b)) 