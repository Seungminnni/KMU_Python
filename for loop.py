for row in range(1,4):
   for i in range(row):
      print("#", end="")
   for i in range(4-row):
      print("$", end="")
   
   print()

for i in range(1,6):
    for k in range(5-i):
        print(".", end="")
    for k in range(i):
        print(str(i), end="")
        
    print()