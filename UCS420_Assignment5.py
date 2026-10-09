
# Assignment 5: NumPy Introduction

import numpy as np

YOUR_NAME = "Keerat"

#  Q1: 
arr1 = np.array([10, 20, 30, 40, 50])
print("Q1: Original array:", arr1)
print("a) Add 2 to every element:", arr1 + 2)
print("b) Multiply every element by 3:", arr1 * 3)
print("c) Divide every element by 2:", arr1 / 2)

# Q2
# a) Reverse the array
arr2 = np.array([1, 2, 3, 6, 4, 5])
print("\nQ2(a): Reversed array:", arr2[::-1])

# b) 
def print_modes_and_indices(array, label):
    values, counts = np.unique(array, return_counts=True)
    max_count = counts.max()
    modes = values[counts == max_count]
    print(f"\n{label}: {array}")
    print("Most frequent value(s):", modes)
    for mode in modes:
        print(f"Indices where {mode} occurs:", np.where(array == mode)[0])

x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])
y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])
print_modes_and_indices(x, "Q2(b)(i) Array x")
print_modes_and_indices(y, "Q2(b)(ii) Array y")

# Q3
arr3 = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print("\nQ3: 2-D array:\n", arr3)
print("a) 1st row, 2nd column:", arr3[0, 1])
print("b) 3rd row, 1st column:", arr3[2, 0])

# Q4 
array_name = f"{YOUR_NAME}"
array_1d = np.linspace(10, 100, 25)
print(f"\nQ4: {array_name} array:", array_1d)
print("Dimensions (ndim):", array_1d.ndim)
print("Shape:", array_1d.shape)
print("Total elements (size):", array_1d.size)
print("Data type:", array_1d.dtype)
print("Total bytes consumed (nbytes):", array_1d.nbytes)

# A 
array_reshaped = array_1d.reshape(5, 5)
print("Reshaped to 5x5:\n", array_reshaped)
print("Transpose using reshape-based 2-D array .T:\n", array_reshaped.T)
print("Can we use .T? Yes. For a 2-D array, .T swaps rows and columns.")
print("Note: array_1d.T is the same as array_1d because a 1-D array has no row/column axes.")

# Q5
values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 15, 20, 35]
ucs420_keerat = np.array(values).reshape(3, 4)
print("\\nQ5: Original ucs420_keerat array:\\n", ucs420_keerat)
print("Mean:", np.mean(ucs420_keerat))
print("Median:", np.median(ucs420_keerat))
print("Maximum:", np.max(ucs420_keerat))
print("Minimum:", np.min(ucs420_keerat))
print("Unique elements:", np.unique(ucs420_keerat))

reshaped_ucs420_keerat = ucs420_keerat.reshape(4, 3)
print("Reshaped to 4 rows and 3 columns:\\n", reshaped_ucs420_keerat)


# Here 12 elements become 6, so the extra elements are discarded.
resized_ucs420_keerat = np.resize(ucs420_keerat, (2, 3))
print("Resized to 2 rows and 3 columns:\\n", resized_ucs420_keerat)
