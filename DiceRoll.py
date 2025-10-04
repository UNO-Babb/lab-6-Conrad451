#DiceRoll.py
#Name:Connor Pell
#Date: 10/4
#Assignment: Lab 6
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0]
  for r in range(10000):#Create two dice values ranging from 1 - 6 each
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    
    #find the sum total of the two dice
    sumtotal = dice1 + dice2
    rolls[sumtotal - 1] = rolls[sumtotal - 1 ] + 1
    #print statictics for dice rolls

  dice = 1
  for count in rolls:
    print(dice, ":", count)
    dice += 1
if __name__ == '__main__':
  main()
