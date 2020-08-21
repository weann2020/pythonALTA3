from cheatdice import *
swapper = Cheat_Swapper()
loaded_dice = Cheat_Loaded_Dice()

cheater = Cheat_Keep_Rolling_6()

swapper_score = 0
loaded_dice_score = 0
cheater_score = 0

number_of_games = 100000
game_number = 0
print("Simulation running")
print("==================")
while game_number < number_of_games:
  swapper.roll()
  loaded_dice.roll()
  cheater.roll()

  swapper.cheat()
  loaded_dice.cheat()
  cheater.cheat()
   #Remove # before print statements to see simulation running
   #Simulation takes approximately one hour to run with print
   #statements or ten seconds with print statements
   #commented out

 #print("Cheater 1 rolled" + str(swapper.get_dice()))
 #print("Cheater 2 rolled" + str(loaded_dice.get_dice()))
  if sum(swapper.get_dice()) == sum(loaded_dice.get_dice()):
 #print("Draw!")
    if sum(swapper.get_dice()) < sum(cheater.get_dice()):
        cheater_score+=1
    else:
        pass
  elif sum(swapper.get_dice()) > sum(loaded_dice.get_dice()):
 #print("Dice swapper wins!")
    if sum(swapper.get_dice()) < sum(cheater.get_dice()):
        cheater_score+=1
    elif sum(swapper.get_dice()) == sum(cheater.get_dice()):
        pass
    else:
        swapper_score+= 1
  else:
    if sum(loaded_dice.get_dice()) < sum (cheater.get_dice()):
        cheater_score+=1
    elif sum(loaded_dice.get_dice()) == sum (cheater.get_dice()):
        pass
    else:
 #print("Loaded dice wins!")
        loaded_dice_score += 1
  game_number += 1
print("Simulation complete")
print("-------------------")
print("Final scores")
print("------------")
print("Swapper won: " + str(swapper_score))
print("Loaded dice won: " + str(loaded_dice_score))
print("Cheater won:" + str(cheater_score))
if swapper_score == loaded_dice_score:
    if swapper_score < cheater_score:
        print("Cheater won most games")
    else:    
        print("Game was drawn")
elif swapper_score > loaded_dice_score:
    if swapper_score < cheater_score:
        print("Cheater won most games")
    elif swapper_score == cheater_score:
         print("Game was drawn")
    else:    
        print("Swapper won most games")
else:
    if loaded_dice_score < cheater_score:
        print("Cheater won most games")
    elif loaded_dice_score == cheater_score:
        print("Game was drawn")
    else:    
        print("Loaded dice won most games")

