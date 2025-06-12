"""
Given an array of integers and a target sum, return a pair of numbers that add up to the target.
If no pair exists, return an empty array.

array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
# Output: [-1, 11] or [11, -1]
"""

# Naive Solution
"""
1. Sort the array
   [-4, -1, 1, 3, 5, 6, 8, 11]
2. Iterate through the array, and find index of compliment if it exists
    itr : 1
    val = -4, compliment = target - val = 14
    idx = array.index(14)
    if ValueError: continue
    else: we have our answer
If we loop through the array and we find nothing, we return an empty array.
"""
# Time Complexity : O(n^2) | Space Complexity : O(1)
def two_sum_naive(array, target):
    answer = []
# .sort() mutates in place    
    # original_array = array 
    # array.sort() # O(n log n)
# instead use sorted(arr) to sort and get a copy
    array = sorted(array)
    for num in array: # O (n)
        compliment = target - num
        try:
            array.index(compliment) # O (n)
            if num == compliment:
                continue
            answer.append(num)
            answer.append(compliment)
            break # We need to break here, since we don't want duplicate answers
        except ValueError:
            continue
    return answer

# Naive Solution - II
# Nested Loops
"""
You can save a few redundant comparisons by making the inner loop start from i+1:

python
Copy
Edit
for i in range(len(array)):
    for j in range(i + 1, len(array)):
This:

Skips checking (j, i) if (i, j) was already checked

Makes the i == j check unnecessary
"""
# Time Complexity : O(n^2) | Space Complexity : O(1)
def two_sum_naive_2(array, target):
    answer = []
    for i in range(len(array)):
        for j in range(len(array)):
            if i == j:
                continue
            if array[i] + array[j] == target:
                answer.append(array[i]) 
                answer.append(array[j])
                return answer
    return answer


# A better solution 
# Since, we can sort the array and look from both sides, we should consider 2-pointer method
# TODO


if __name__ == "__main__":
    arr = [3, 5, -4, 8, 11, 1, -1, 6]
    target = 10
    print(two_sum_naive(arr, target))
    print(two_sum_naive_2(arr, target))
