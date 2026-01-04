from Array import *

val = array('i',[1,2,3,4,5,6,7,8])
abc = val[3: 7]
for i in range(0, len(abc)):
    print(abc[i], end=" ")

copyArray = array(val.typecode,(x*3 for x in val))

copyArray.pop(3)
copyArray.remove(15)

for i in range(0, len(copyArray)):
    print(copyArray[i], end=" ")

#abc = val[startIndex:endIndex]
