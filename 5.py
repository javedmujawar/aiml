import numpy as np

arr1 = np.array([1,2,3,4,5])

print(arr1)
print(type(arr1))

arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)

print(arr1.shape)
print(arr2.shape)

print(arr1[0])
print(arr2[1,2])


arr3 = np.array([2,4,6,8,10])

print(arr3 + arr3)
print(arr3 * arr3)
print(np.sin(arr1))

arr4 = np.array([1,2,3,4,5,6])
reshaped_arr = arr4.reshape((2,3))
print(reshaped_arr)

sequence = np.arange(1,10,2)
print(sequence)

print(np.max(arr4))
print(np.min(arr4))
print(np.mean(arr4))
print(np.sum(arr4))

arr5 = np.array([[1,2,3],[4,5,6]])
transposed_arr = np.transpose(arr5)
print(transposed_arr)
