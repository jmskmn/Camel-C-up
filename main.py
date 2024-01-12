import random
class Camel:
  def __init__(self, color, board):
    self.color = color
    self.board = board
  def move(self, distance):
    for i, space in enumerate(self.board):
      if self in space:
        e = space[space.index(self):]
        for camel in e:
          self.board[i].remove(camel)
          self.board[i+distance].append(camel)
        break
  def __repr__(self) -> str:
    return self.color + " camel"
  

class Die:
  def __init__(self, color):
    self.value = -1
    self.color = color
  def rollDie(self):
    val = int(random.random() *3//1 + 1)
    self.value = val
    return val
  
class Bet:
  def __init__(self, amount, type, camel = 0):
    self.amount = amount
    self.type = type
    self.camel = camel


class Player:
  def __init__(self, board):
    self.money = 0
    self.bets = []
  
  def placeCamelBooster(self,index):
    #TODO
    return
  def placeCamelSabatage(self,index):
    #TODO
    return
  

  
  #Takes roll card that gives one coin
  def takeRollCard(self):
    #adds the b et to player to be resolved at end of round
    self.bets.append(Bet(1,"roll"))
    
    #Pulls a dice then moves the camel that distance and updates rolled/notrolled
    dice = random.choice(notrolled)
    notrolled.remove(dice)
    camels[dice.color].move(dice.rollDie())
    print(str(camels[dice.color]) + " moved " + str(dice.value))
    

    return
  def placeBet(self,color):
    #TODO
    return


def endOfLeg():
  notrolled = rolled
  rolled = []
  return
#TODO: Function that handles what happens at the end of each leg. Should go through all players and payout bets, etc.


def getCamelCell(color, board):
  for i, space in enumerate(board):
    for camel in space:
      if camel.color == color:
        return i


#
#Sets up game board and makes the initial rolls
#
  
#Preparing Data structures
board = [[] for x in range(19)]
#I made the board have 19 slots, we only use the first 16 slots (up to index 15) but the last 3 slots are used to check for win condition(if any camels are in those slots)
colors = ["blue","yellow","white","orange","green"]
camels = {}#points a color to a camel camels["green"] will access the green camel object
rolled = []#represents rolled dice
notrolled = [Die(color) for color in colors]#represents unrolled dice

#Makes initial rolls
for i in range(5):
  dice = random.choice(notrolled)
  rolled.append(dice)
  notrolled.remove(dice)
  camel= Camel(dice.color, board)
  camels[dice.color] = camel
  board[dice.rollDie()-1].append(camel)

notrolled = rolled
rolled = []


print(board)
p = Player(board)
p.takeRollCard()
print(board)
