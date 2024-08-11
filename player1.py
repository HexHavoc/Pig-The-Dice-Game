import random

class Player1:
     def __init__(self):
          self.max_score = 20
          self.player_1_name = input("Enter the name for player 1:")
          self.player_2_name = input("Enter the name for player 2:")
          self.player_1_point = 0
          self.player_2_point = 0

     def dice_roll(self):
          self.dice_number = random.randint(1,6)
          return self.dice_number
        

     def confirm_dice_roll(self):
          dice_roll_choice = input("Roll the dice(y or n)?:")
          if(dice_roll_choice.lower() == 'y'):
               self.player_1_point += self.dice_roll()

          else:
               print(f"Current Score of {self.player_1_name} is {self.player_1_point}")
        

     def 