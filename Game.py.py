import random
import time

print("###  WELCOME TO STONE, PAPER, SCISSOR GAME  ###\n")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
i = 0



while True:    
    entry = input("Type 0 for Rock, 1 for Paper, 2 for Scissors or press Enter to exit: ")
    pose = [rock, paper, scissors]
    
    if entry == "":
        print(f"Your Score is {i}, Thanks for playing!")
        if i<0:
            print("Computer Wins :)")
        elif i == 0:
            print("Match Draw !!!")
        else:
            print("Hurray, You Win :)")
        break
    elif entry not in ["0", "1", "2"]:
        print("Invalid number, You lose!\n")
        i -= 1
    else:
        entry = int(entry)  
        print(pose[entry])
    
        print("Computer chose:")
    
        pc = random.randint(0,2)
        print(pose[pc])
        
        if entry == pc:
            print("Draw\n")
        elif (entry==0 and pc==2) or (entry==1 and 
            pc==0) or (entry==2 and pc==1):
            i += 1
            print("You Won\n")
        else:
            print("You lose\n")
            i -= 1
        
time.sleep(3)        