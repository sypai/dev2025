"""
Arrays in Python - Basics
DSA Topic: Arrays (Python Lists)
"""

print("========== 1. What is an Array ==========\n")

basic_array = [1, 2, 3, 4, 5]
print("Array:", basic_array)
print("Access by index [0]:", basic_array[0])  # Output: 1

# TODO: Create your own list and access an element

print("\n========== 2. Indexing ==========\n")

arr = [10, 20, 30, 40, 50]
print("Positive indexing arr[2]:", arr[2])      # 30
print("Negative indexing arr[-1]:", arr[-1])    # 50
print("Negative indexing arr[-3]:", arr[-3])    # 30

# TODO: Access third last element using negative indexing

print("\n========== 3. Slicing ==========\n")

slice_array = [5, 10, 15, 20, 25, 30]
print("Original:", slice_array)
print("Slice [2:5]:", slice_array[2:5])         # [15, 20, 25]
print("Slice [::2]:", slice_array[::2])         # [5, 15, 25]
print("Reversed [::-1]:", slice_array[::-1])    # [30, 25, 20, 15, 10, 5]

# TODO: Slice to get middle 4 elements of a 10-element array

print("\n========== 4. Looping ==========\n")

# Value-based loop
print("Looping by value:")
for value in slice_array:
    print("Value:", value)

# Index-based loop
print("\nLooping by index:")
for i in range(len(slice_array)):
    print(f"Index {i}, Value {slice_array[i]}")

# TODO: Loop and print only even values

print("\n========== 5. Modifying In-Place ==========\n")

mod_array = [1, 2, 3, 4, 5, 6]
print("Original array:", mod_array)

for i in range(len(mod_array)):
    if mod_array[i] % 2 == 0:
        mod_array[i] = mod_array[i] * 2

print("Modified (even numbers doubled):", mod_array)

# TODO: Modify odd numbers to be squared in the array below
arr = [1, 2, 3, 4, 5, 6]

print("\n========== END OF FILE ==========")
