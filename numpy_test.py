import numpy as np

a = np.array([4, 5, 6])
# print(a)
# print(a.shape)
# print(a.size)
# print(a[0])
# print(a[0:2])
# d = np.expand_dims(a, axis=1)
# print(d)
b = np.array([1, 2, 3])
c = np.vstack((a, b))
print(c.shape)
# on = np.ones((1, 3, 5))
# print(on)
# print(np.hstack((a, b)))

test = np.array([[1, 3, 4, 5], [3, 4, 5, 6], [1, 2, 3, 4]])
print(test.reshape(3, -1))
