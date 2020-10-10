


"""Calculates the temperature closest to zero
​
Write a program that prints the temperature closest to 0 among input data. If two numbers are equally close to zero, positive integer has to be considered closest to zero (for instance, if the temperatures are -5 and 5, then display 5)
​
https://www.codingame.com/ide/puzzle/temperatures
"""
num_temps = input()
temperatures = list(map(int, input().split()))
​# Method 1
min_temp = temperatures[0] if temperatures else 0
​
for temperature in temperatures:
  if abs(temperature) < abs(min_temp):
    min_temp = temperature
​
# Method 2
min_temp = min(temperatures, key=abs, default=0)
​
print(abs(min_temp) if abs(min_temp) in temperatures else min_temp)
​
# if abs(min_temp) in temperatures:
#   print(abs(min_temp))
# else:
