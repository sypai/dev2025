"""
🧩 Problem: Three Sum (Generic)

Given an array of integers `nums` and a target integer `target`,
return all **unique triplets** `[a, b, c]` in the array such that:
    a + b + c == target

Return the triplets in any order.  
Each triplet must be unique (no duplicates).

---

🔧 Function Signature:
def three_sum(nums: list[int], target: int) -> list[list[int]]:
    pass

---

📥 Example:
Input: nums = [-1, 0, 1, 2, -1, -4], target = 0  
Output: [[-1, -1, 2], [-1, 0, 1]]

Input: nums = [1, 2, -2, -1], target = 0  
Output: []

---
"""

# NAIVE SOLUTION
"""
Find all unique triplets, check if sum is equal to target
return all such triplets
"""
# Time Complexity : O(n^3) | Space : O(n^3)
def three_sum_naive(nums: list[int], target: int) -> list[list[int]]:
    answer = set()
    length = len(nums)

    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                if nums[i] + nums[j] + nums[k] == target:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    answer.add(triplet)  # set avoids duplicates

    return [list(t) for t in answer]


# SOLUTION : Using Hash-Map
# Time Complexity : O(n^2) | Space Complexity : O(n)
"""
Here's a problem with this approach
I can get [-4, 2, 2] which is wrong as I only have a single '2'
"""
def three_sum_hash(nums: list[int], target: int):
    memory = {}
    answer = set()
    for num in nums:
        if not (target - num) in memory:
            memory[target - num] = "look for a sum that equals me"

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            current_sum = nums[i] + nums[j]
            if current_sum in memory:
                triplet = tuple(sorted([nums[i], nums[j], target - current_sum]))
                answer.add(triplet)
    return [list(t) for t in answer]

# Time Complexity : O(n^2) | # Space Complexity : O(n)
def three_sum(nums: list[int], target: int):
    nums.sort()
    answer = []
    
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # skip duplicate i

        left = i + 1
        right = len(nums) - 1

        while left < right:
            currentSum = nums[i] + nums[left] + nums[right]

            if currentSum == target:
                answer.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                # skip duplicates on left
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                # skip duplicates on right
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif currentSum < target:
                left += 1
            else:
                right -= 1

    return answer

if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    # nums = [12, 3, 1, 2, -6, 5, -8, 6]
    target = 0  
    print(three_sum(nums, target))
