"""
Your objective is to write a program capable of predicting
the route Indy will take on his way down a tunnel. Indy is
not in danger of getting trapped in this first mission.

https://www.codingame.com/ide/puzzle/the-last-crusade-episode-1

"""
ROOM_TYPES = {
    0: {},
    1: {
        "LEFT": "BOTTOM",
        "TOP": "BOTTOM",
        "RIGHT": "BOTTOM",
    },
    2: {
        "LEFT": "RIGHT",
        "RIGHT": "LEFT",
    },
    3: {
        "TOP": "BOTTOM",
    },
    4: {
        "TOP": "LEFT",
        "RIGHT": "BOTTOM",
    },
    5: {
        "TOP": "RIGHT",
        "LEFT": "BOTTOM",
    },
    6: {
        "LEFT": "RIGHT",
        "RIGHT": "LEFT",
    },
    7: {
        "TOP": "BOTTOM",
        "RIGHT": "BOTTOM",
    },
    8: {
        "LEFT": "BOTTOM",
        "RIGHT": "BOTTOM",
    },
    9: {
        "LEFT": "BOTTOM",
        "TOP": "BOTTOM",
    },
    10: {
        "TOP": "LEFT",
    },
    11: {
        "TOP": "RIGHT",
    },
    12: {
        "RIGHT": "BOTTOM",
    },
    13: {
        "LEFT": "BOTTOM",
    },
}
ACTIONS = {
  "LEFT": [0, -1],
  "RIGHT": [0, 1],
  "BOTTOM": [1, 0],
}
WIDTH, HEIGHT = list(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(HEIGHT)]
EXIT_POSITION = input()
while True:
  x, y, direcion = input().split()
  x = int(x)
  y = int(y)
  type_of_cell = grid[y][x]
  exit_direction = ROOM_TYPES[type_of_cell][direcion]
  action = ACTIONS[exit_direction]
  print(x + action[1], y + action[0] )

