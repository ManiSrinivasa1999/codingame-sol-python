"""
Calculate Nearest Position
The city of Montpellier has equipped its streets with
defibrillators to help save victims of cardiac arrests.
The data corresponding to the position of
all defibrillators is available online.

Based on the data we provide in the tests,
write a program that will allow users to find
the defibrillator nearest to their location using their mobile phone.

https://www.codingame.com/ide/puzzle/defibrillators
"""
import math

EARTH_RADIUS = 6371

def calculate_distance(point1, point2):
  """
  Calculates the distance between point1 and point2
  """
  lng1, lat1 = point1
  lng2, lat2 = point2
  x = (lng2 - lng1) * math.cos((lat1 + lat2) / 2)
  y = lat2 - lat1
  distance = math.sqrt(x ** 2 + y ** 2) * EARTH_RADIUS
  return distance

user_lng = float('.'.join(input().split(',')))
user_lat = float('.'.join(input().split(',')))
user_point = (user_lng, user_lat)
no_of_def = int(input())
defibrilators = {}

for _ in range(no_of_def):
  d_id, name, address, contact, lng, lat = input().split(';')
  defibrilators[d_id] = {
    'name': name,
    'address': address,
    'contact': contact,
    'lng': float('.'.join(lng.split(','))),
    'lat': float('.'.join(lat.split(','))),
    'point': (float('.'.join(lng.split(','))), float('.'.join(lat.split(',')))),
  }
nearest_defibrilator = min(defibrilators.values(),
                        key=lambda defibrilator:
                        calculate_distance(user_point,
                                          defibrilator['point']))
print(nearest_defibrilator['name'])
