#1
import numpy as np

#2
print(np.zeros(10))

#3
print(np.ones(10))

#4
print(np.ones(10)*5)

#5
print(np.arange(10,51))

#6
arr = np.arange(10,51)
bool_arr = arr%2 == 0
print(arr[bool_arr])

#7
print(np.arange(0,9).reshape((3,3)))

#8
print(np.eye(3))

#9
print(np.random.rand(1))

#10
print(np.random.randn(25))

#11
print(np.arange(1,101)/100)

#12
print(np.linspace(0,1,20))

#13
mat = np.arange(1,26).reshape(5,5)
print(mat[2:,1:])

#14
print(mat[3,4])

#15
print(mat[0:3,1:2])

#16
print(mat[4:,:])

#17
print(mat[3:,:])

#18
print(mat.sum())

#19
print(np.std(mat))

#20
print(np.sum(mat,0))