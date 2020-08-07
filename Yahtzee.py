import random

#max_rolls defines how many 6-sided dice to roll
#dice is a list to store the results
def roll_dice(max_rolls, dice):
  for i in range(0, max_rolls):
    roll = random.randint(1, 6)
    dice[i] = roll

#validate_choice checks the user input values from reroll
#if they are valid, they are converted to ints and return true
#dice is a list that contains ints of the original roll
#reroll is a list that contains strings that the user input
def validate_choice(dice, reroll):
  valid = True

  if len(reroll) > len(dice):
    valid = False
    return valid

  for i in range(0, len(reroll)):
    if len(reroll[i]) > 1:
      valid = False
      return valid
    
    if reroll[i].isdigit():
      reroll[i] = int(reroll[i])
    else:
      valid = False
      return valid

  return valid

#replace_rolls checks if the user input values exist in the 
#original dice list
#returns true if all values are successfully rerolled
def replace_rolls(dice, reroll):
  for i in range(0, len(dice)):
    if dice[i] in reroll:
      reroll.remove(dice[i])
      dice[i] = random.randint(1, 6)

  if len(reroll) == 0:
    return True
  else:
    return False
