"""
💰 Problem: Non-Constructible Change
You're given an array of positive integers coins. Each integer represents a coin of that value.
Write a function that returns the minimum amount of change that cannot be created using any combination of the coins.

Example 1:

Input: coins = [1, 2, 5]
Output: 4
# You can make 1, 2, 3 (1+2), 5, 6 (1+5), 7 (2+5), 8 (1+2+5)
# But not 4.

Example 2:

Input: coins = [5, 7, 1, 1, 2, 3, 22]
Output: 20


Constraints:
1 <= len(coins) <= 1e4

1 <= coins[i] <= 1e4
"""


# NAIVE SOLUTION

"""
- sort the array
- have two indexes - from & to
- have a loop counter (change) that starts from 1,
    while True:
        we continue with counter + 1, if we find the counter (change) as a sum of sub-arrays from and to
        whichever number we don't find as change we'll have it when we have had all possible sums in array
"""
def non_constructible_change_naive(coins: list[int]) -> int:
    memory = {}
    change = 1
    fromIdx = 0
    toIdx = 0
    while fromIdx <= len(coins) and toIdx <= len(coins):
        print(f"{fromIdx}:{toIdx}")
        if change in memory:
            continue
        subArray = coins[fromIdx:toIdx+1]
        print(subArray)
        currentSum = sum(subArray)
        if change == currentSum:
            memory[change] = "constructible"
            change += 1
            toIdx += 1
            continue
        memory[currentSum] = "constructible"
        if currentSum > change:
            fromIdx += 1

# Greedy Solution
# Trick, sort and run a current change sum
# if the next coin is greater currentChangeSum + 1
# currentChangeSum is the min non-constructible change
def non_constructible_change(coins):
    coins.sort()
    currentChangeCreated = 0

    for coin in coins:
        if coin > currentChangeCreated + 1:
            return currentChangeCreated + 1
        currentChangeCreated += coin

    return currentChangeCreated + 1


if __name__ == "__main__":
    coins = [1, 2, 5]
    print(non_constructible_change(coins))

