import numpy as np

#ref https://note.nkmk.me/python-numpy-matrix/

# sec-1
print("sec-1 =============")
print ("yes")

arr1 = np.arange(4)
print("arr1 => ", arr1)

arr1 = np.arange(4).reshape((2, 2))
print("arr1 => ", arr1)

# sec-2
print()
print("sec-2 =============")
arr1 = np.matrix([1, 1])
arr2 = np.matrix([0, 1, 2,3])
arr3 = np.matrix([0, 1, 4,5])
arr1_1 = arr1.reshape((2,1))
arr2_1 = arr2.reshape((2,2))
arr3_1 = arr3.reshape((2,2))

print("arr2 => ", arr2)
print("arr1_1 => ", arr1_1)
print("arr2_1 => ", arr2_1)
print("arr3_1 => ", arr3_1)

# sec-3
print()
print("sec-3 =============")

#dot_1_3 = np.dot(arr1_1,arr2_1)
dot_2_1 = np.dot(arr2_1,arr1_1)
print("dot_2_1 (np.dot(arr2_1,arr1_1)) => ", dot_2_1)

dot_3_1 = np.dot(arr3_1,arr1_1)
print("dot_3_1 (np.dot(arr3_1,arr1_1)) => ", dot_3_1)
