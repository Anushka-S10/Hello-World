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


# Arrays and Exponents
import numpy as np
arr1 = np.array([1,2,3])
arr2 = arr1**2
arr3 = arr1**3
print('arr1:',arr1)
print('arr2:',arr2)
print('arr3:',arr3)


# Math Operations and Arrays
import numpy as np
arr1 = np.array([1,2,3])
sqrt = np.sqrt(arr1)
log1 = np.log(arr1)
exp1 = np.exp(arr1)
print('sqrt:',sqrt)
print('log1:',log1)
print('exp1:',exp1)


# Working with “-1” Subranges with Vectors
import numpy as np
# -1 => "all except the last element in …" (row or col)
arr1 = np.array([1,2,3,4,5])
print('arr1:',arr1)
print('arr1[0:-1]:',arr1[0:-1])
print('arr1[1:-1]:',arr1[1:-1])
print('arr1[::-1]:', arr1[::-1]) # reverse!


# Working with “-1” Subranges with Arrays
import numpy as np
# -1 => "the last element in …" (row or col)
arr1 = np.array([(1,2,3),(4,5,6),(7,8,9),(10,11,12)])
print('arr1:', arr1)
print('arr1[-1,:]:', arr1[-1,:])
print('arr1[:,-1]:', arr1[:,-1])
print('arr1[-1:,-1]:',arr1[-1:,-1])


# Arrays and Vector Operations

import numpy as np
a = np.array([[1,2], [3, 4]])
b = np.array([[5,6], [7,8]])
print('a: ', a)
print('b: ', b)
print('a + b: ', a+b)
print('a _ b: ', a_b)
print('a * b: ', a*b)
print('a / b: ', a/b)
print('b / a: ', b/a)
print('a.dot(b):',a.dot(b))


# NumPy and Dot Products (1)

import numpy as np
a = np.array([1,2])
b = np.array([2,3])
dot2 = 0
for e,f in zip(a,b):
    dot2 += e*f
print('a: ',a)
print('b: ',b)
print('a*b: ',a*b)
print('dot1:',a.dot(b))
print('dot2:',dot2)


import numpy as np
a = np.array([1,2])
b = np.array([2,3])
print('a: ',a)
print('b: ',b)
print('a.dot(b): ’,a.dot(b))
print('b.dot(a): ',b.dot(a))
print('np.dot(a,b):',np.dot(a,b))
print('np.dot(b,a):',np.dot(b,a))

