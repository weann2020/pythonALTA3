from random import randint

class Player:
  def __init__(self):
    self.dice = []

  def roll(self):
    self.dice = [] # clears current dice
    for i in range(3):
      self.dice.append(randint(1,6))

  def get_dice(self):
    return self.dice

class Cheat_Swapper(Player):
  def cheat(self):
    self.dice[-1] = 6

class Cheat_Loaded_Dice(Player):
  def cheat(self):
    i = 0
    while i < len(self.dice):
      if self.dice[i] < 6:
        self.dice[i] += 1
      i += 1

class Cheat_Keep_Rolling_6(Player):      
    def cheat(self):
        i=0
        for i in range(len(self.dice)):
           while self.dice[i]<6:
              self.dice.remove(self.dice[i])
              self.dice.append(randint(1,6))
              
player = Player()
cheater = Cheat_Keep_Rolling_6()

player.roll()
cheater.roll()

cheater.cheat()


print("Player rolled" + str(player.get_dice()))
print("Cheater rolled" + str(cheater.get_dice()))

if sum(player.get_dice()) == sum(cheater.get_dice()):
  print("Draw!")

elif sum(player.get_dice()) > sum(cheater.get_dice()):
  print("Player wins!")

else:
  print("Cheater wins!")
