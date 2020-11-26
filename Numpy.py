# import package numpy

# Appending Elements to Arrays 
import numpy as np
arr1 = np.array([1,2,3])
# these do not work:
#arr1.append(4)
#arr1 = arr1 + [5]
arr1 = np.append(arr1,4)
arr1 = np.append(arr1,[5])
for e in arr1:
    print(e)
arr2 = arr1 + arr1
for e in arr2:
    print(e)


# Appending Elements to Arrays
import numpy as np
arr1 = np.array([1,2,3])
arr1 = np.append(arr1,4)
for e in arr1:
    print(e)
arr1 = np.array([1,2,3])
arr1 = np.append(arr1,4)
arr2 = arr1 + arr1
for e in arr2:
    print(e)


# Multiply Lists and Arrays
import numpy as np
list1 = [1,2,3]
arr1 = np.array([1,2,3])
print('list: ',list1)
print('arr1: ',arr1)
print('2*list:',2*list)
print('2*arr1:',2*arr1)


# Doubling the Elements in a List
import numpy as np
list1 = [1,2,3]
list2 = []
for e in list1:
    list2.append(2*e)
print('list1:',list1)
print('list2:',list2)


import numpy as np
list1 = [1,2,3]
list2 = []
for e in list1:
list2.append(e*e) # e*e = squared
print('list1:',list1)
print('list2:',list2)

