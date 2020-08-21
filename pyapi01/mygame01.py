#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
  do [action]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
#  print(str(room[currentRoom]['description']))
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:     
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []
actions = []

#a dictionary linking a room to other rooms
rooms = {

            'Hall' : { 
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'west'  : 'Master Bed Room',
                  'item'  : 'key',
                  'description' : 'This is the start point and also the hub of the rooms'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'south' : 'Basement',
                  'item'  : 'monster',
                  'description' : 'Danger! Be cautious! You need a gun to survive in here!'
                },
            'Dining Room' : {
                  'west'  : 'Hall',
                  'south' : 'Garden',
                  'item'  : 'potion',
                  'description' : 'Don\'t forget to pick up something here!'
                },
            'Master Bed Room' : {
                  'east' : 'Hall',
                  'south': 'Bath Room',
                  'item' : 'gun',
                  'action' : 'jump',
                  'description' : 'Don\'t forget to pick up something here! You can also jump through the window into the garden!'
                },
            'Bath Room' : {
                  'north' : 'Master Bed Room',
                  'item'  : 'shower',
                  'description' : 'You can take a shower here!'
                },
            'Basement' : {
                  'north' : 'Kitchen',
                  'item'  : 'gas mask',
                  'description' : 'This is a dead end! Don\'t forget to pick up something here!'
                },
            'Gas Chamber' : {
                  'north' : 'Dining Room',
                  'south' : 'Garden',
                  'description' : 'This is the gas chamber. You wil die if you don\'t have a gas mask...'
                },
            'Garden' :{
                  'north' : 'Dining Room',
                  'description' : 'This is the ending point of this game'
                }

         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()
  print(str(rooms[currentRoom]['description']))
  print("----------------------------------------------------------------------")

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':  
    move = input('>')
  
  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
#      print(str(rooms[currentRoom]['description']))
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')
  print(str(rooms[currentRoom]['description']))
  print("---------------------------------------------------------------------")

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')

  if move[0] == 'do':
      if 'action' in rooms[currentRoom] and move[1] in rooms[currentRoom]['action']:
          actions += [move[1]]
          print(move[1] + 'done!')
      else:
          print('Can\'t do '+ move[1] + '!')
#  if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
#      print('A monster has got you... GAME OVER!')
#      break
  if currentRoom == 'Kitchen':
      if 'gun' in inventory:
          print("Monster has been killed...You are safe now!")
      else:
          print('A monster has got you... GAME OVER!')
          break
  if currentRoom == 'Gas Chamber':
      if 'gas mask' in inventory:
          print("You survived the gas chamber with the gas mask.")
      else:
          print("You are dying in this gas chamber without a gas mask....GAME OVER!")
          break
  if currentRoom == 'Garden':
      if 'key' in inventory and 'potion' in inventory and 'shower' in inventory:
          print('You escaped the house with the ultra rare key, the  magic potion, and you took a shower after the gas chamber...YOU WIN!')
          break
      else:
          print("You either didn't get all the required items or you forgot to take a shower after the gas chamber...GAME OVER!")
          break
  if currentRoom == 'Master Bed Room':
      if 'jump' in actions:
          currentRoom == 'Gargen'
          print("You just jumped into the Garden!")
