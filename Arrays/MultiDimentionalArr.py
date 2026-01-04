from numpy import *
#zero dimensional array only holds a single value
zero = array(10)
print(zero)
#one dimensional array holds a list of values
one = array([1,2,3,4,5])
print(one)
#two dimensional array holds rows and columns
#It is a collection of 1D arrays
two = array([[1,2,3],[4,5,6],[7,8,9]])
print(two)
#three dimensional array holds multiple 2D arrays. 
#It is a collection of 2D arrays
three = array([[[1,2],[3,4],[7,8]],[[11,12],[14,16],[17,18]]])
print(three)