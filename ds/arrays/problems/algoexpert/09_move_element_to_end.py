"""
🧠 Problem: Move Element to End

Given an array of integers and a specific value `toMove`, 
move all instances of that value to the end of the array **in-place**.

The order of the other elements does not matter.

You must perform this with **O(1)** extra space.

---

Function Signature:
    def move_element_to_end(array: list[int], toMove: int) -> list[int]:

---

Example:
    Input:
        array = [2, 1, 2, 2, 2, 3, 4, 2]
        toMove = 2
    Output:
        [4, 1, 3, 2, 2, 2, 2, 2]
        # Any valid arrangement with all 2s at the end is acceptable

---

Constraints:
- Do not use extra lists.
- Must be done in-place.
- Order of non-`toMove` elements can be changed.
"""

# Problem: Move Element to End
# Write a function that takes in a list of integers and a target value (`toMove`).
# Move all instances of that target value to the **end** of the list in-place.
# The relative order of other elements does **not** matter.
# The operation must be done with **O(1)** extra space.

# Function Signature:
# def move_element_to_end(array: list[int], toMove: int) -> list[int]:

# Sample Input:
# array = [2, 1, 2, 2, 2, 3, 4, 2]
# toMove = 2

# Sample Output:
# [4, 1, 3, 2, 2, 2, 2, 2]
# (Any valid arrangement with all 2s at the end is correct.)

# Explanation:
# There are 5 instances of `2`, which must be moved to the end of the array.
# The rest of the elements can appear in any order before them.

# Constraints:
# - Perform the operation in-place (no extra lists).
# - Use constant extra space.
# - It’s okay if the order of non-`toMove` elements changes.

def move_element_to_end(array: list[int], toMove: int) -> list[int]:
    left = 0
    right = len(array) - 1
    while right > left:
        if array[left] == toMove:
            if array[right] == toMove:
                right -= 1
                continue
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
        else:
            left += 1
    return array 

# Test Case
if __name__ == "__main__":
    arr = [2, 1, 2, 2, 2, 3, 4, 2]
    print(move_element_to_end(arr, 2))
    # Expected Output: [4, 1, 3, 2, 2, 2, 2, 2]
    # (Order of [4, 1, 3] can vary; all 2s must be at the end)
