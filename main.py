#Yahtzee! by Peach
#This program simulates turns in the game Yahtzee
#The player rolls 5 dice and has the option to reroll any 
#number of the values
#The player can reroll their dice a total of 2 times before ending their turn
#This game does not currently keep score
import Yahtzee
from os import system
keep_playing = True
input("Welcome to Yahtzee, press enter to begin!")

#one iteration represents a player's turn
while keep_playing:
  system("clear")
  dice = [0, 0, 0, 0, 0]
  num_rolls = 5

  Yahtzee.roll_dice(num_rolls, dice)
  print("Roll:", dice)
  keep_rolling = True
  num_rerolls = 0

  #one iteration represents one reroll 
  #the user can reroll a maximum of 2 times before ending the turn
  while keep_rolling and num_rerolls < 2:
    reroll = input("Enter the values to reroll separated by spaces:\nor press enter to skip the reroll: ")
    reroll = reroll.split()
    
    #if the user enters a blank string,
    #they end their turn without rerolling
    if reroll == []:
      keep_rolling = False
    else:
      choice_valid = Yahtzee.validate_choice(dice, reroll)
      if choice_valid:
        is_replaced = Yahtzee.replace_rolls(dice, reroll)
        if is_replaced:
          print("New Roll:", dice)
          num_rerolls += 1
        else:
          print("Error rerolling, please enter valid dice values")
      else:
        print("Error rerolling please enter valid dice values")


  exit = input("Turn ended, press e to exit or enter to continue: ")
  if exit == "e":
    system("clear")
    print("Thanks for playing!")
    keep_playing = False

