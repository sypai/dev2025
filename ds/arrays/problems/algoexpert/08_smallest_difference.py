# Problem: Smallest Difference
# Write a function that takes in two non-empty arrays of integers and returns a pair of numbers 
# (one from each array), whose absolute difference is closest to zero.
# Return the pair in any order.
# You may assume there will be exactly one pair with the smallest difference.

# Function Signature:
# def smallest_difference(arrayOne: list[int], arrayTwo: list[int]) -> list[int]:

# Sample Input:
# arrayOne = [-1, 5, 10, 20, 28, 3]
# arrayTwo = [26, 134, 135, 15, 17]

# Sample Output:
# [28, 26]

# Explanation:
# Absolute difference between 28 and 26 is 2, which is the smallest possible.

# Constraints:
# - Both arrays are non-empty
# - Exactly one pair will have the smallest absolute difference
# - Arrays may be of different lengths
# - Numbers can be positive or negative

"""
NAIVE SOLUTION

- find all possible pairs and keep a track of smallest difference
""" 
# Time Complexity : O(n^2) | Space Complexity : O(1)
def smallest_difference_naive(arrayOne: list[int], arrayTwo: list[int]) -> list[int]:
    smallestDifference = float("inf")
    pair = [0, 0]

    for one in arrayOne:
        for two in arrayTwo:
            diff = abs(one - two)
            if diff < smallestDifference:
                smallestDifference = diff
                pair[0] = one
                pair[1] = two
    return pair

# Time Complexity : O (n log n) {n is the size of bigger array} | Space Complexity : O(1)
def smallest_difference_rToL(arrayOne: list[int], arrayTwo: list[int]) -> list[int]:
    smallestDifference = float("inf")
    pair = [0, 0]

    arrayOne.sort() # O (n log n)
    arrayTwo.sort() # O (m log m)

    one = len(arrayOne) - 1
    two = len(arrayTwo) - 1

    while one >= 0 and two >= 0: # O (n + m) 
        diff = abs(arrayOne[one] - arrayTwo[two])
        if diff < smallestDifference:
            smallestDifference = diff
            pair[0] = arrayOne[one]
            pair[1] = arrayTwo[two]

        if arrayOne[one] > arrayTwo[two]:
            one -= 1
        else:
            two -= 1
    return pair


### IT MAKES MORE SENSE TO GO FROM LEFT TO RIGHT
def smallest_difference(arrayOne: list[int], arrayTwo: list[int]) -> list[int]:
    arrayOne.sort()
    arrayTwo.sort()

    i = 0
    j = 0
    smallest = float("inf")
    pair = []

    while i < len(arrayOne) and j < len(arrayTwo):
        first = arrayOne[i]
        second = arrayTwo[j]
        diff = abs(first - second)

        if diff < smallest:
            smallest = diff
            pair = [first, second]

        if first < second:
            i += 1
        elif first > second:
            j += 1
        else:
            return [first, second]  # absolute diff is 0

    return pair


# Test Case
if __name__ == "__main__":
    a1 = [-1, 5, 10, 20, 28, 3]
    a2 = [26, 134, 135, 15, 17]
    print(smallest_difference(a1, a2))  # Expected Output: [28, 26]
