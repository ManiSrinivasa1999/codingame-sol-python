"""Finds the horses closest Strength
Casablanca’s hippodrome is organizing a new type of horse racing:
duals. During a dual, only two horses will participate in the race.
In order for the race to be interesting, it is necessary to try
to select two horses with similar strength.

Write a program which, using a given number of
strengths, identifies the two closest strengths and
shows their difference with an integer (≥ 0).

https://www.codingame.com/ide/puzzle/horse-racing-duals
"""

number_of_horses = int(input())
horses_strengths = sorted([int(input()) for _ in range(number_of_horses)])
differences = [abs(horses_strengths[i] - horses_strengths[i+1])
                for i in range(len(horses_strengths) - 1)]
print(min(differences))
