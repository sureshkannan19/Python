import numpy as np
np.set_printoptions(suppress=True)

np_array = np.array([1, 2, 3])
py_array = [1, 2, 3]
print(np_array == py_array)

print(np.zeros(5)) # initialize array filled with defined number of zeros

print(np.linspace(start=0, stop=5, num=5)) # (end - start) / (num - 1)

# Analogy: let's say i have 7 kids and have 10 mil, and need to split up the money between them
shares = np.linspace(start=0, stop=10000000, num=8)
diff = np.diff(shares)
print(diff)


import matplotlib.pyplot as plt

total = 10_000_000
kids = 7

# Equal split with integer handling
share = total // kids
distribution = np.full(kids, share)
distribution[: total % kids] += 1

# Plot
plt.bar(range(1, kids+1), distribution)
plt.xlabel("Kid Number")
plt.ylabel("Share Amount")
plt.title("Distribution of 10 Million Among 7 Kids")
plt.show()