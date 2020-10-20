"""
https://www.codingame.com/ide/puzzle/sokoban

Place all boxes on their target cells.
 	Rules
You have one unit which you can move around on the map.
You can push boxes by walking into them. This will push
the box in the same direction as you are moving in.
The field where you push the box to must be free,
it is not possible to move two or more boxes at once.
You are given target cells where you have to place the boxes.
 	Expert Rules
The source code can be found here: https://github.com/eulerscheZahl/Sokoban
 	Game Input
Initial input
Line 1: width height boxCount, the width and
height of the map and the number of boxes

next height lines: a string of width characters, that can be:

. for an empty cell
# for a wall
* for a target cell
Input per turn
Line 1: pusherX pusherY, the position of your unit

next boxCount lines: boxX boxY, the position of each box

Output
A single character indicating your movement direction:
U to move up, D to move down, R to move right, L to move left.
Constraints
7 ≤ width ≤ 11
7 ≤ height ≤ 11
3 ≤ boxCount ≤ 5

Allotted response time to output is ≤ 10 seconds
for the first turn, 50 ms for later turns.
"""

def build_solution(visted, current_goal_state):
  """
  """
  pass

def check_goal():
  """
  """
  pass
  # 

def valid_move():
  """
  """
  pass
  # returns true if the move is valid

# operator
def calculate_possible_moves():
  """
  """
  pass
  # number of possible moves for a node 
  # return all valid nodes

def search(node, visited, fringe):
  """Returns solution

  Args:
    node<dict>: contains info about parent and state
    visited<dict>: contains info about visited nodes
    fringe<list>: list of nodes to be explored
  Returns:
    solution<string>: movesto reach from  initial state to goal state
  """
  while fringe:
    root_node = fringe[0]
    fringe = fringe[1:]
    possible_moves = calculate_possible_moves()
    for possible_move in possible_moves:
      if possible_move['state'] in visited:
        continue
      else:
        if check_goal(possible_move['state']):
          return build_solution(visited, possible_move)
        else:
          fringe.append(possible_move)
  # current state of graph
  # calculate possible moves
  # check each possible is in visited
  # if move already in visited discard else append it to fringe if not goal
  # access parent of goal state till the initial node is reached
  # Eg: node = {'parent': '##0*', 'state': '*0###', 'move': 'U'}
  # Eg: visited = {'*0###': {'parent': '##0*', 'state': '*0###', 'move': 'U'}}
  # Eg: fringe = [{'parent': '##0*', 'state': '*0###', 'move': 'U'}]

width, height, box_count = [int(i) for i in input().split()]
for i in range(height):
  line = input()

# game loop
while True:
  pusher_x, pusher_y = [int(i) for i in input().split()]
  for i in range(box_count):
    box_x, box_y = [int(j) for j in input().split()]
  # find a solution using search
  # print each step in solution

