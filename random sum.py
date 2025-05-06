import random

terms = random.randint(2, 5)
sum = 0
for i in range(terms):
   term = random.randint(1, 10)
   print(str(term) + " + ", end=" ")
   sum += term
   
user_sum = int(input(" = "))

if sum == user_sum:
   print("You are correct")
   
else:
   print("You are wrong! :(")

    

