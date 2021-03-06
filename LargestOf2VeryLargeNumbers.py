'''
    This is a python program to check the largest of two very large numbers,
    i.e, numbers of the form x^y(512^513, 613^614) which we'll not be able to find using the coneventional
    methods. We do this by taking the log of the number and then checking for the largest.
    We use the result  x^y = y.log(x).

'''


import math                

def res(x,y):                              #Function to find the result(log) of given exponent.
    if x and y !=0:
        return y*math.log10(x)             # We use the relation x^y = y*log10(x), where 10 is the base.
    else:
        if(x==0):                          # 0 raised to any number is 0
            return 0
        elif(y==0):
            return 1                       # any number raised to 0 is 1

# Reads two numbers from input and typecasts them to int using map function.
# Here x is the base and y is the power.
x1,y1 = map(int, input().split(','))
x2,y2 = map(int, input().split(','))

# We find the log of each number, using the function res(), which takes two arguments.
res1=res(x1,y1)
res2=res(x2,y2)

# We check for the largest number            
if(res1>res2):
    print("Largest number is",x1,'^',y1)
elif(res2>res1):
    print("Largest number is", x2, '^', y2)
else:
    print("Both are equal")
