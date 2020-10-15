import sys
import math
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def connected_gears(gear_1, gear_2):
    """Returns wheather gear_1 and gear_2 are connected
    Args:
        gear_1(tuple(int x, int y, int r)): info about gear 1
        gear_2(tuple(int x, int y, int r)): info about gear 2
    Returns:
        conneted(boolean): wheather gear_1 and gear_2 are connected
    """
    x1, y1, r1 = gear_1
    x2, y2, r2 = gear_2
    distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    return distance == r1 + r2
n = int(input())
gears = []
for i in range(n):
    x, y, r = [int(j) for j in input().split()]
    # store gears
    gears.append((x, y, r))
neighbours = {}
# neighbour => (1, 2, 3): set((4, 5, 6),(7, 8, 9))
# compute all neighbors of each gear
for gear_1 in gears:
    for gear_2 in gears:
        if connected_gears(gear_1, gear_2):
            if gear_1 in neighbours:
                neighbours[gear_1].add(gear_2)
            else:
                neighbours[gear_1] = set([gear_2])
            if gear_2 in neighbours:
                neighbours[gear_2].add(gear_1)
            else:
                neighbours[gear_2] = set([gear_1])
rotations = {}
rotations[gears[0]] = 'CW'
to_explore = [gears[0]]
visited = set()
while to_explore:
    root_node = to_explore[0]
    visited.add(root_node)
    to_explore = to_explore[1:]
    current_neighbours = neighbours[root_node]
    not_moving = False
    for neighbour_1 in current_neighbours:
        for neighbour_2 in current_neighbours:
            if neighbour_2 in neighbours[neighbour_1]:
                not_moving = True
                break
        if not_moving:
            break
    if not_moving:
        break
    else:
        if rotations[root_node] == 'CW':
            for neighbour in current_neighbours:
                rotations[neighbour] = 'CCW'
        elif rotations[root_node] == 'CCW':
            for neighbour in current_neighbours:
                rotations[neighbour] = 'CW'
    for neighbour in current_neighbours:
        if neighbour not in visited:
            to_explore.append(neighbour)
last_gear = gears[-1]
if last_gear in rotations and not_moving == False:
    print(rotations[last_gear])
else:
    print('NOT MOVING')
# for each neighbour of root node compute it's rotation
# expand until no nodes are left
# print the direction of last gear