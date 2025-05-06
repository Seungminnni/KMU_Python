import random


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
   print("You are correct")
   
else:
   print("You are wrong! :(")
   
