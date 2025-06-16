"""
Problem: Sorted Squared Array

Given an array of integers `array` sorted in non-decreasing order, 
return a new array of the squares of each number, also sorted in non-decreasing order.

You must build the resulting array with **O(n)** time complexity if possible.

Example 1:
Input: array = [-4, -1, 0, 3, 10]
Output: [0, 1, 9, 16, 100]

Example 2:
Input: array = [-7, -3, 2, 3, 11]
Output: [4, 9, 9, 49, 121]

Constraints:
- 1 <= array.length <= 10^4
- -10^4 <= array[i] <= 10^4
- array is sorted in non-decreasing order
"""

# Naive Solution
"""
we loop through our input array and append the squares in our output array
we sort
this would be O(n log n)
"""
# Time Complexity: O(n log n) |  Space Complexity: O(n)
def sorted_squared_naive(arr):
    squared = []
    for num in arr:
        squared.append(num * num)
    squared.sort()
    return squared

# Two Pointers
"""
- we loop through the array to find the first positive integer, that is our anchor index
- we square the num here and put it as the first number in our squared array
- now, we take two pointers, left and right
    left = anchor - 1
    right = anchor + 1
        we loop, while left >= 0 and right < len(arr):
    
            we check the absolute value of element at both indexes, 
            if abs(arr[left]) < abs(arr[right])
                we append the square of arr[left]
                and left -= 1
            if abs(arr[left]) > abs(arr[right])
                we append the square of arr[right]
                and right += 1
            if abs(arr[left]) == abs(arr[right])
                we append square of arr[left] 
                we append the square of arr[right]
                left -= 1
                right += 1
        if left < 0:
            for i in range(right, len(arr)):
                squared.append(arr[i] * arr[i])
        if right = len(arr):
            for i in range(left, 0, -1):
                squared.append(arr[i] * arr[i]) 
    and return our output array

    Time Complexity gets reduced to O(n)
"""

"""
You're thinking like an engineer—anchoring at the first non-negative number, expanding outwards.

But there's unnecessary complexity: we can simplify this with left = 0 and right = len(arr) - 1, 
and build the output from end to start based on absolute values.

Your version has two edge bugs:

= You append the anchor's square only once, not placing it in the correct sorted order.
= Final for loop range(left, 0, -1) misses index 0 and is logically reversed.
"""
# Time Complexity: O(n) |  Space Complexity: O(n)
def sorted_squared(arr):
    squared = []
    anchor = 0
    while anchor < len(arr):
        if arr[anchor] >= 0:
            squared.append(arr[anchor] * arr[anchor])
            break
        anchor += 1

    left = anchor - 1
    right = anchor + 1

    while left >= 0 and right < len(arr):
        valL = abs(arr[left])
        valR = abs(arr[right])

        if valL < valR:
            squared.append(valL * valL)
            left -= 1
        if valL > valR:
            squared.append(valR * valR)
            right += 1
        if valL == valR:
            squared.append(valL * valL)
            squared.append(valR * valR)
            left -= 1
            right += 1

    if left < 0:
        for i in range(right, len(arr)):
                squared.append(arr[i] * arr[i])
    
    if right == len(arr):
            for i in range(left, 0, -1):
                squared.append(arr[i] * arr[i]) 

    return squared

# Time: O(n) | Space: O(n)
def sorted_squared_array(arr):
    result = [0] * len(arr)
    # another way to create an array for another array's length is
    # result = [0 for _ in array]
    left = 0
    right = len(arr) - 1
    i = len(arr) - 1  # We fill from the end

    while left <= right:
        left_val = abs(arr[left])
        right_val = abs(arr[right])

        if left_val > right_val:
            result[i] = left_val ** 2
            left += 1
        else:
            result[i] = right_val ** 2
            right -= 1
        i -= 1

    return result


if __name__ == "__main__":
    arr1 = [-4, -1, 0, 3, 10]
    print("sorted squared array 1 : ", sorted_squared(arr1))
    arr2 = [-7, -3, 2, 3, 11]
    print("sorted squared array 2 : ", sorted_squared(arr2))