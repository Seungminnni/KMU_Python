import random
tries = 0
sum = 0
while sum != 7:
   dice1 = random.randint(1, 6)
   dice2 = random.randint(1, 6)
   sum = dice1 + dice2
   tries += 1
   print(str(dice1)+ " + "+str(dice2) + " == " + str(sum))
   
if sum == 7:
   print("You won after " + str(tries)+ " tries!")