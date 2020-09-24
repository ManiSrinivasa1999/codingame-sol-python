"""
The goal for your program is to safely land the "Mars Lander"
shuttle, the landing ship which contains the Opportunity rover.
Mars Lander is guided by a program, and right now the failure
rate for landing on the NASA simulator is unacceptable.

For more details: https://www.codingame.com/ide/puzzle/mars-lander-episode-1
"""


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def desired_thrust(velocity):
  if abs(velocity) > 39:
    rover_power = 4
  elif abs(velocity) <=39:
    rover_power = 3
  return rover_power
# the number of points used to draw the surface of Mars.
surface_n = int(input())

for i in range(surface_n):
  # land_x: X coordinate of a surface point. (0 to 6999)
  # land_y: Y coordinate of a surface point. By linking all
  # the points together in a sequential fashion, you form the surface of Mars.
  land_x, land_y = [int(j) for j in input().split()]

# game loop
while True:
  # h_speed: the horizontal speed (in m/s), can be negative.
  # v_speed: the vertical speed (in m/s), can be negative.
  # fuel: the quantity of remaining fuel in liters.
  # rotate: the rotation angle in degrees (-90 to 90).
  # power: the thrust power (0 to 4).
  x, y,h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

  # Write an action using print
  # To debug: print("Debug messages...", file=sys.stderr, flush=True)


  # 2 integers: rotate power. rotate is the desired rotation
  # angle (should be 0 for level 1), power is the
  # desired thrust power (0 to 4).
  print(0,desired_thrust(v_speed))
