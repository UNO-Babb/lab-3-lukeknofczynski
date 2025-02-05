#RPS.py
#Name: Luke Knofczynski
#Date: 2/5/25
#Assignment: 
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  play = "Y"
  while play == "Y":
    
    player = input("Enter Rock(R), Paper(P), or Scissors(S): ")
    
    computer = random.choice(["R", "P", "S"])
    
    print("Computer choose:", computer)
    if player == "R":
      if computer == "R":
        print("Tie!")
        ties = ties + 1
      if computer == "S":
        print("You Win!")
        wins = wins + 1
      if computer =="P":
        print("You Lose!")
        losses = losses +1
    elif player == "P":
      if computer == "P":
        print("Tie!")
        ties = ties + 1
      if computer == "R":
        print("You Win!")
        wins = wins + 1
      if computer =="S":
        print("You Lose!")
        losses = losses +1
    elif player == "S":
      if computer == "S":
        print("Tie!")
        ties = ties + 1
      if computer == "P":
        print("You Win!")
        wins = wins + 1
      if computer =="R":
        print("You Lose!")
        losses = losses +1
    else:
      print("Invaild Input")

    play = input("play again? (Y/N): ")
  print("Thanks for Playing")
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
