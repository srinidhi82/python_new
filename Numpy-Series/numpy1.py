import numpy as np

data = np.array([1,8,5,9,2])

print(f"The values of the array is: {data}")
print("Sum of arrays", np.sum(data))

squared = data **2
print(squared)

print("Mean of elements:", np.mean(data))        # Mean of all elements
print("Standard deviation:", np.std(data))  