"""Optimize the number of ghosts caught by busters
"""
import random
import math
IDLE = 'idle'
CAN_CATCH = 'can_catch'
HAS_GHOST = 'has_ghost'
SEE_GHOST = 'see_ghost'
def calculate_next_point(buster):
  """Returns the next point buster will move to in the current direction
  Args:
    buster(dict): Info regarding buster
  Returns:
    point(int, int): point to which buster will move
  """
  x = buster['x']
  y = buster['y']
  direction = buster['direction']
  distance = 800
  next_x = int(x + distance * math.cos(math.radians(direction)))
  next_y = int(y + distance * math.sin(math.radians(direction)))
  return (next_x, next_y)
def calculate_distance(point1, point2):
  """Return the distance between point 1 and point 2
  Args:
    point1(int, int): coordinates of point1 x, y
    point2(int, int): coordinates of point2 x, y
  Returns:
    distance(int): distance between point1, point2 rounded to nearest integer
  """
  x1, y1 = point1
  x2, y2 = point2
  return int(((y2 - y1)**2 + (x2 - x1)**2)**0.5)
def update_state(buster, ghosts, opponents):
  """Return the current state of buster
  Args:
    buster(dict): Our buster information
    ghosts(dict): Information about all visible ghosts
    opponents(dict): Information about all visible opponents
  """
  visible_ghosts = []
  catchable_ghosts = []
  for ghost in ghosts.values():
    ghost_distance = calculate_distance((buster['x'], buster['y']), (ghost['x'], ghost['y']))
    if ghost_distance < 2200:
      visible_ghosts.append(ghost)
    if ghost_distance <= 1760 and ghost_distance >= 900:
      catchable_ghosts.append(ghost)
  visible_opponents = []
  catchable_opponents = []
  for opponent in opponents.values():
    opponent_distance = calculate_distance(
        (buster['x'], buster['y']), (opponent['x'], opponent['y']))
    if opponent_distance < 2200:
      visible_opponents.append(opponent)
    if opponent_distance <= 1760 and opponent_distance >= 900:
      catchable_opponents.append(opponent)
  buster['catchable_ghosts'] = catchable_ghosts
  buster['visible_ghosts'] = visible_ghosts
  buster['visible_opponents'] = visible_opponents
  buster['catchable_opponents'] = catchable_opponents
  if buster['value'] != -1:
    buster['current_state'] = HAS_GHOST
    return buster
  elif catchable_ghosts:
    buster['current_state'] = CAN_CATCH
    return buster
  elif visible_ghosts:
    buster['current_state'] = SEE_GHOST
    return buster
  else:
    buster['current_state'] = IDLE
    return buster
WIDTH = 16000
HEIGHT = 9000
number_of_busters = int(input())
number_of_ghosts = int(input())
team_id = int(input())
our_team = {}
our_opponents = {}
all_ghosts = {}
while True:
  no_of_entities = int(input())
  all_ghosts = {}
  for _ in range(no_of_entities):
    enitity_id, x, y, entity_type, state, value = list(map(int, input().split()))
    if entity_type == team_id:  # our buster
      if enitity_id in our_team: # game update
        our_team[enitity_id].update({
            'x': x,
            'y': y,
            'state': state,
            'value': value,
        })
      else: # initial input
        our_team[enitity_id] = {
            'id': enitity_id,
            'x': x,
            'y': y,
            'state': state,
            'value': value,
        }
    elif entity_type == -1:  # ghost
      all_ghosts[enitity_id] = {
          'id': enitity_id,
          'x': x,
          'y': y,
          'state': state,
          'value': value,
      }
    else:
      if enitity_id in all_ghosts:  # game update
        our_opponents[enitity_id].update({
            'x': x,
            'y': y,
            'state': state,
            'value': value,
        })
      else:
        our_opponents[enitity_id] = {
            'id': enitity_id,
            'x': x,
            'y': y,
            'state': state,
            'value': value,
        }
  for team_member in our_team:
    # update state
    team_member = update_state(our_team[team_member], all_ghosts, our_opponents)
    member_state = team_member['current_state']
    if member_state == HAS_GHOST:
      base = (0, 0) if team_id == 0 else (16000, 9000)
      distance_to_base = calculate_distance((team_member['x'], team_member['y']),
                                  (base[0], base[1]))
      if distance_to_base < 1600:
        print('RELEASE')
      else:
        print(f'MOVE {base[0]} {base[1]}')
    elif member_state == CAN_CATCH:
      ghost_to_bust = team_member['catchable_ghosts'][0]
      print(f'BUST {ghost_to_bust["id"]}')
    elif member_state == SEE_GHOST:
      ghost_to_catch = team_member['visible_ghosts'][0]
      print(f'MOVE {ghost_to_catch["x"]} {ghost_to_catch["y"]}')
    elif member_state == IDLE:
      if 'direction' in team_member:
        # calculate the next point to move to
        next_x, next_y = calculate_next_point(team_member)
        if next_x > 16000 or next_x < 0 or next_y < 0 or next_y > 9000:
          direction = random.randint(0, 359)
          team_member['direction'] = direction
        next_x, next_y = calculate_next_point(team_member)
        print(f'MOVE {next_x} {next_y}')
      else:
        direction = random.randint(0, 359)
        team_member['direction'] = direction
        next_x, next_y = calculate_next_point(team_member)
        print(f'MOVE {next_x} {next_y}')
    # choose action
    # one of the following
    # MOVE X Y
    # BUST GHOST_ID
    # RELEASE