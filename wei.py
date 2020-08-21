ideas={"number":"12",
        "name":"python",
        "frequency":"30"
        }
num = int(ideas["number"])
freq = int(ideas["frequency"])

#Guess 1
print("Chad just thought of some number in his mind. Please take a guess what it is.")
counter = 3
answer = " "

while counter > 0 and answer != 12:
  counter -= 1
  guess = input("Please enter your guess: ")
 # if guess != "" and isinstance(guess, int):
  if guess != "":
      answer = int(guess)
  else:
      print("Warning: no/wrong input! $100 fine if this happens again...")
      break
  if answer == num:
      print("Bingo! You can read Chad's mind!")
  elif counter == 0:
      print("Sorry, it's number 12. Next...")
  elif answer < num and answer > 0:
      print("It's bigger than you think. Guess again!")
  elif answer > num:
      print("It's smaller than you think. Guess again!")
  else:
      print("Sorry, wrong answer. It's a number. Guess again!")

#Guess 2
print("What is Chad's favorite coding language? ")
counter = 3
answer = " "
while counter > 0 and answer != "python":
    counter -= 1
    guess = input("Please enter your guess: ")
    if guess != "":
        answer = str(guess)
    else:
        print("Warning: no input! $50 fine if this happens again...")
        break 
    if answer.lower() == ideas["name"]:
        print("Bingo! You can read Chad's mind!")
    elif counter == 0:
        print("Sorry, it's Python. Next...")
    elif answer.lower() == "javascript":
        print("That's his second favorite! Guess again!")
    elif answer.lower() == "java":
        print("That was his favorite but not anymore. Guess again!")
    else:
        print("Sorry, wrong answer. It's a coding language. Guess again!")

#Guess 3
print("How often does Chad smile? Every __ seconds or so?")
counter = 3
answer = " "
while counter > 0 and answer != 30:
  counter -= 1
  guess = input("Please enter your guess: ")
  #if guess != "" and isinstance(guess, int):
  if guess != "":
      answer = int(guess) 
  else:
      print("Warning: no/wrong input! $100 fine if this happens again...") 
      break
  if answer == freq:
      print("Bingo! Good observation!")
  elif counter == 0:
      print("Sorry, he smiles every 30 seconds or so...Next")
  elif answer < freq and answer > 0:
      print("He is happy but not that happy... Guess again!")
  elif answer > freq:
      print("He definitely smiles more often that that... Guess again!")
  else:
      print("Sorry, wrong answer. It's a number. Guess again!")
