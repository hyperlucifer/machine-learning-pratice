# numpy is a numerical python libery
# Allows several mathmacial operations 
# faster operations 
import numpy as np
from time import process_time
# list vs numpy array

# time taken by list
py_List=[i for i in range(1000)]
st_time=process_time()
py_List=[i+5 for i in py_List]
end_time=process_time()

print(end_time-st_time)

# time for numpy array
np_array=np.array([i for i in range(1000)])
st_time=process_time()
np_array+=5
end_time=process_time()
print(end_time-st_time)

# np_array
np_array1=np.array([1,2,3,4,5,6],dtype="int32")#you can pass any sequence
print(type(np_array1))

# creating multi-dimenshal arrays

#1d
a=np.array([1,2,3,4])
print(a.shape)

#2d
b=np.array([(1,2,3,4),(7,6,5,4)])
print(b.shape)
print(b)

# initial placeholders in numpy arrays 
# means the initial values present in that numpy array.vc4

# array with all the zeros 

z=np.zeros((4,5))
print(z)

# array with all the ones

o=np.ones((3,5))
print(o)

# array of a perticular value

p=np.full((3,4),98)
print(p)

# identity matrix

i=np.eye(5)
print(i)

# numpy arrays with randam values

r=np.random.random((3,4))# it will give randam values 0-1
print(r)

# random integer value array with a range
rI=np.random.randint(5,11,(3,4))
print(rI)

# array of eveny spaced values 
ev=np.linspace(21,100,10) # provided starting ,ending value,and the number of values
print(ev) 

#  array of eveny spaced values --> with step
es=np.arange(3,29,4)
print(es)

# a list to numpy array
li=[1,2,3,4,5,6]
arrLi=np.asarray(li)
print(arrLi)
print(type(arrLi))

# # analysing numpy array

ana=np.random.randint(10,65,(5,5))
# the shape of the array 
print(ana.shape) 
# total number of elements
print(ana.size)

# number of diamasions
print(ana.ndim)

# checking data type of an array
print(ana.dtype)

# # mathematical operations on np array

a1=np.random.randint(0,10,(3,3))
b1=np.random.randint(10,20,(3,3))
print(a1)
print(b1)

# element wise arithmatic operations

print(a1+b1)
print(a1-b1)
print(a1/b1)
print(a1*b1)
  
# # array manipulation
array=np.random.randint(0,10,(2,3))
print(array)

# transpose of the array 
trans=np.transpose(array)
print(trans)

sorted_arr = np.sort(array)
sorted_indices = np.argsort(array)
print(sorted_arr)
print(sorted_indices)
