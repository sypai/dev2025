# Problem: Monotonic Array
# Write a function that takes in an array of integers and returns a boolean indicating whether the array is monotonic.
# An array is monotonic if it is entirely non-increasing or entirely non-decreasing.

# Sample Input:
# array = [1, 2, 2, 3]

# Sample Output:
# True

# Sample Input:
# array = [5, 4, 4, 2, 1]

# Sample Output:
# True

# Sample Input:
# array = [1, 3, 2]

# Sample Output:
# False

# Explanation:
# - [1, 2, 2, 3] is non-decreasing → monotonic
# - [5, 4, 4, 2, 1] is non-increasing → monotonic
# - [1, 3, 2] switches direction → not monotonic

# Constraints:
# - You can assume the array has at least one element
# - Elements may be equal
# - Must return True for both strictly and non-strictly increasing/decreasing sequences

# Your Implementation Starts Below:
def is_monotonic(array: list[int]) -> bool:
    if len(array) == 1:
        return True

    monotonicType = ""
    idx = 0
    while idx <= len(array) - 2:
        diff = array[idx] - array[idx + 1]
        if diff == 0:
            idx += 1
            continue
        if monotonicType == "":
            if diff > 0:
                monotonicType = "decreasing"
            else:
                monotonicType = "increasing"
            idx += 1
            continue
        else:
            if diff > 0 and monotonicType == "increasing":
                return False
            elif diff < 0 and monotonicType == "decreasing":
                return False
        idx += 1
    return True


# Test Case
if __name__ == "__main__":
    print(is_monotonic([1, 2, 2, 3]))     # True
    print(is_monotonic([5, 4, 4, 2, 1]))  # True
    print(is_monotonic([1, 3, 2]))        # False
