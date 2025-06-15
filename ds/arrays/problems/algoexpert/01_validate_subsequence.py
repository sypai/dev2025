"""
Given two arrays: array and sequence, write a function to determine 
if the sequence is a valid subsequence of the array.

A subsequence of an array is a set of elements that appear in the same order as they appear in the array, but not necessarily contiguously.

For example:

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]  # ✅ Valid subsequence
sequence = [5, 22, 8]      # ✅ Valid
sequence = [1, 10, -1]     # ❌ Invalid (wrong order)
"""

# Starting with Two Pointers
"""
arr1 = [5, 1, 22, 25, 6, -1, 8, 10]
arr2 = [5, 22, 8]

- if len(arr2) > len(arr1)
    return false
- we start with 2 pointers, i and j
    i=0, j=0
    
    we loop with our loop control being i < len(arr1):
        if arr1[i] == arr2[j]
            if j == len(arr2) - 1
                return true
            if j < len(arr2)
                i += 1
                j += 1
        else
            i += 1
    return false    
"""
# Time Complexity : O (n) where n is the size of array1 | Space Complexity : O (1)
def validate_subsequence(arr1, arr2):
    len1 = len(arr1)
    len2 = len(arr2)
    if len2 > len1:
        return False
    i = 0
    j = 0
    while i < len1: # O (n) where n is the size of array1
        if arr1[i] == arr2[j]:
            if j == len2 - 1:
                return True
            elif j < len2:
                i += 1
                j += 1
        else:
            i += 1
    return False 


if __name__ == "__main__":
    arr1 = [5, 1, 22, 25, 6, -1, 8, 10]
    # arr2 = [5, 22, 8] # True
    arr2 = [1, 10, -1] # False
    print(validate_subsequence(arr1, arr2))

