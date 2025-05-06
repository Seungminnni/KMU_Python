height=2

def main():
   draw_box()
   
def draw_box(): #height

   top_bottom_line()
   for i in range(height):
      middle_line()
   top_bottom_line()

def middle_line(): ##width
   print("|", end="")
   print(20*" ", end="") 
   print("|")
   
def top_bottom_line():
   print("+", end="")
   print(10*"/\\", end="")
   print("+")

main()