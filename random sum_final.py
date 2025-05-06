import random

def main():
   total_points = 0
   total_losses = 0
   
   while total_losses !=3:
      points = single_game()
      total_points += points  #counts points
      if points == 0:
         total_losses +=1 #counts lisses
   print("You earned " + str(total_points)+ " points")


def single_game():
   terms = random.randint(2, 5)
   
   term = random.randint(1, 10)
   print(str(term), end=" ")
   sum = term
      
   for i in range(terms-1):
      term = random.randint(1, 10)
      print(" + " + str(term), end ="")
      sum += term
      
   user_sum = int(input(" = "))
   
   if sum == user_sum:
      return 1
      
   print("Wrong! The answer was" + str(sum))
   return 0
      
main()