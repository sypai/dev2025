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
"""
- we sort the array, let's say in increasing order
  [-4, -1, 1, 3, 5, 6, 8, 11]
- we have a pointer i, starting from left side of the array, idx = 0
- we have another pointer j, starting from right side

- we check sum of arr[i] + arr[j] and compare it to target
    if sum = target: we have our answer
    if sum < target: 
        like -4 (i=0) and 11 (j=7), sum=7 < 10, 
        we know we need to increase the sum
        which can be done increasing i by 1, and checking again
        i=i+1, i=1
        now, -1 (i=1) and 11 (j=7), sum=10 = 10 
        we have our answer
    if sum > target:
        we decrease j by 1
    what if we don't get sum==targetSum, where do we stop?
    when i==j
"""
# Time Complexity : O (n log n) | Space Complexity : O (1)
def two_sum_two_pointer(array, target):
    answer = []
    i = 0
    j = len(array) - 1
    array = sorted(array) # O (n log n)
    while i < j: # O (n)
        currentSum = array[i] + array[j]
        
        if currentSum < target:
            i += 1
        elif currentSum > target:
            j -= 1
        else:
            answer.append(array[i])
            answer.append(array[j])
            break
    return answer

"""

"""

if __name__ == "__main__":
    arr = [3, 5, -4, 8, 11, 1, -1, 6]
    target = 10
    # print(two_sum_naive(arr, target))
    # print(two_sum_naive_2(arr, target))
    print(two_sum_two_pointer(arr, target))
