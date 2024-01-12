import random

class Die:
  def __init__(self, color):
    self.value = -1
    self.color = color
  def rollDie(self):
    val = int(random.random() *3//1 + 1)
    self.value = val
    return val



board = [[] for x in range(16)]
colors = ["blue","yellow","white","orange","green"]
rolled = []
camels = {"blue":-1,"yellow":-1,"white":-1,"orange":-1,"green":-1}
notrolled = [Die(color) for color in colors]
for i in range(5):
  dice = random.choice(notrolled)
  rolled.append(notrolled.remove(dice))
  camels[dice.color] += dice.rollDie()
  board[camels[dice.color]].append(dice.color)
notrolled = rolled
rolled = []

print(board)
