from numpy import *
#numpy gives us the facility to create heterogeneous arrays
#that is arrays with different data types
#here we create an array with integers, floats and strings
val = array ([1,2,3,4.5,5,6.9,7,8,'a'])
for x in val:
    print(x, end=" ,")

#val= linspace(0,15,10) # 10 values between 0 to 15
#val= arange(1,15,2) # values between 1 to 15 with a step of 2
#val= logspace(1,40,5) # 5 values between 10^1 to 10^40
#val= zeros(5) # array of 5 zeros
#val= ones(5) # array of 5 ones
#val= full(10,5) # array of 10 fives