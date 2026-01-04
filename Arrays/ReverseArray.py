from array import *

val = array('i', [1,2,3,4,5,6,7,8])
val.reverse()
for i in range(0, len(val)):
    print(val[i], end= " ,")

print('\n')

val.insert(2,50)
val.append(100)
val[3] = 200 #replace

for i in range(0, len(val)):
    print(val[i], end=" ,")