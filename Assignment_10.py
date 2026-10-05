import numpy as np

# Create a one-dimensional array containing numbers from 1 to 10
arr = np.arange(1, 11)

print("Array:", arr)

# Slicing operations
print("First 5 elements:", arr[:5])
print("Last 5 elements:", arr[5:])
print("Elements from index 3 to 6:", arr[3:7])
print("Alternate elements:", arr[::2])

# Statistical measures
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# Broadcasting
arr = arr + 7
print("Array after adding 7 using broadcasting:", arr)

arr = arr * 5
print("Array after multiplying by 5 using broadcasting:", arr)



"""
Array: [ 1  2  3  4  5  6  7  8  9 10]
First 5 elements: [1 2 3 4 5]
Last 5 elements: [ 6  7  8  9 10]
Elements from index 3 to 6: [4 5 6 7]
Alternate elements: [1 3 5 7 9]
Sum: 55
Mean: 5.5
Maximum: 10
Minimum: 1
Array after adding 7 using broadcasting: [ 8  9 10 11 12 13 14 15 16 17]
Array after multiplying by 5 using broadcasting: [40 45 50 55 60 65 70 75 80 85]
"""
