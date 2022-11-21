# Mean Median and Mode using Python
lst=[15,12,34,54,67,67,32,10,23]


                            # Mean
# The mean is the average value of all the values in a dataset.
mean=sum(lst)/len(lst)
print("MEAN: ",mean)


                            # Median
# The Median is the middle value among all the values in sorted order.
# There are two different ways of calculating the median value based on odd and even numbers of elements

# when the total number of values is even: Median  = [(n/2)th term + {(n/2)+1}th]/2
# when the total number of values is odd: Median = {(n+1)/2}th term

lst1=[15,12,34,54,67,67,32,10,23,45]
lst1.sort()
if len(lst1)%2==0:
    m1=lst1[len(lst1)//2]
    m2=lst1[(len(lst1)+1)//2]
    median=(m1+m2)/2
else:
    median=lst1[len(lst1)//2]
print("Median: ",median)


                            # Mode
# Mode is the most frequently occurring value among all the values.
list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
frequency = {}
for i in list1:
    frequency.setdefault(i, 0)
    frequency[i]+=1

frequent = max(frequency.values())
for i, j in frequency.items():
    if j == frequent:
        mode = i
print("Mode",mode)