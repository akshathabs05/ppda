import numpy as np
arr= np.random.randint(1,21, size=(3,3))
print("original array",arr)
mean= np.mean(arr)
print("mean of array",mean)
arr[arr 210]=0
print("modified array:",arr)
