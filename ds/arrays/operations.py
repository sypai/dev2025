"""
Arrays in Python - Common Operations
DSA Topic: Arrays (Python Lists)
"""

print("========== 1. Updating ==========\n")

arr = [1, 3, 5, 7, 9]
print("Original:", arr)

# Safe update: Update 3rd element (index 2)
if len(arr) > 2:
    arr[2] = 50
print("After updating 3rd element to 50:", arr)

# Multiply all odd numbers by 3
for i in range(len(arr)):
    if arr[i] % 2 != 0:
        arr[i] *= 3
print("After multiplying odds by 3:", arr)

# Attempt to update invalid index
try:
    arr[10] = 100
except IndexError:
    print("❌ Error: Tried to update arr[10] → IndexError")

print("\n========== 2. Deletion ==========\n")

arr = ["suyash", "array", "python", 42, "gpt", "delete-me", "last"]
print("Original:", arr)

# Remove by value
arr.remove("delete-me")
print("After remove('delete-me'):", arr)

# Pop index 3
arr.pop(3)
print("After pop(3):", arr)

# Delete first two elements
del arr[0:2]
print("After del arr[0:2]:", arr)

print("\n========== 3. Searching ==========\n")

arr = [5, 3, 8, 3, 9, 1]
print("Array:", arr)

# Search with 'in'
if 9 in arr:
    print("Found 9 using 'in'")

# Search using .index()
print("Index of first 3:", arr.index(3))

# Manual linear search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print("Linear search index of 1:", linear_search(arr, 1))

# Using index() for a missing element
try:
    arr.index(10)
except ValueError:
    print("10 not found using .index() → ValueError")

print("\n========== END OF FILE ==========")
