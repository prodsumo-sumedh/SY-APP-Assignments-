import pandas as pd
import random

# Create a Series with 10 random numbers (1 to 100)
numbers = [random.randint(1, 100) for i in range(10)]
s = pd.Series(numbers)

print("Pandas Series:")
print(s)

# Indexing
print("\nFirst element:", s[0])
print("Last element:", s[9])

# Filtering
print("\nNumbers greater than 50:")
print(s[s > 50])

# Statistical Operations
print("\nMean:", s.mean())
print("Median:", s.median())
print("Minimum:", s.min())
print("Maximum:", s.max())

'''output:
Pandas Series:
0    12
1    78
2    45
3    91
4    33
5    67
6    54
7    29
8    85
9    40
dtype: int64

First element: 12
Last element: 40

Numbers greater than 50:
1    78
3    91
5    67
6    54
8    85
dtype: int64

Mean: 53.4
Median: 49.5
Minimum: 12
Maximum: 91         '''
