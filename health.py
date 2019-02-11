import random
import math

health = 50

difficulty = 3   # difficulty: easy = 1, meduim = 2 or hard = 3

potion_health = int(random.randint(25, 50) / difficulty)  # casting with int

health = health + potion_health
print(health)

squared = math.pow(3, 2)
print(squared)
