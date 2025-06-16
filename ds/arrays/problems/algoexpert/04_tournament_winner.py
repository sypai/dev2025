"""
📝 Problem Statement
You're given two inputs:

A list of matches between teams. Each match is a list of two teams:
matches = [["TeamA", "TeamB"], ["TeamC", "TeamD"], ...]
results = [0, 0, 1]
A corresponding list of results:

1 means the first team in the match won
0 means the second team won

Example: 

matches = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
]

results = [0, 0, 1]

Return the team with the highest total number of wins (3 points per win).
"""

"""
# Intuitively, I can think of a Hash-Map based solution
# Since, the length of two arrays is going to be same, 
# we can loop through both from the same loop.
# Getting inside the sub-array (the individual matches)
# we'll see if both times are present in hash map
# if not : we add the team and give the winning team, 3 points
# if it is present : we simply increment the points
#
# Ah, but how will we compare the values of the keys in hashmap
# we'll need the maximum.
#
# Maybe we can do this, 
# We keep track of the highest points (maybe that's why points per win is mentioned)
# and which team has the highest
#
# Each time we update the entries in our map, we also increment these two variables
# In the end, we'll have our winner

# YAY! It's correct!
"""
# Time Complexity : O (n) | Space Complexity : O (m) # number of teams
def tournament_winner(matches, results):
    highestScore = 0
    winner = ""
    memory = {}
    
    for idx in range(len(results)): # O (n)
        # Which teams are currently fighting?
        match = matches[idx] 

        # Who is the winner?
        if results[idx] == 0:
            currentWinner = match[1]
        else:
            currentWinner = match[0]

        # Update scores
        for team in match:
            if team in memory:
                if team == currentWinner:
                    newScore = memory[team] + 3
                    memory[team] = newScore

                    if newScore > highestScore:
                        highestScore = newScore
                        winner = team
            else:
                memory[team] = 0
                if team == currentWinner:
                    memory[team] = 3

    return winner

# There is a refined version of this, home & away
def tournament_winner(matches, results):
    scores = {}
    currentBest = ""
    scores[currentBest] = 0

    for i in range(len(matches)):
        home, away = matches[i]
        winner = home if results[i] == 1 else away

        scores[winner] = scores.get(winner, 0) + 3

        if scores[winner] > scores[currentBest]:
            currentBest = winner

    return currentBest


if __name__ == "__main__":
    matches = [
        ["HTML", "C#"],
        ["C#", "Python"],
        ["Python", "HTML"]
    ]

    results = [0, 0, 1]

    print(tournament_winner(matches, results))
