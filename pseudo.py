"""
#================# line()
|      <><>      |
|    <>....<>    |
|  <>........<>  |
|<>............<>| draw_top
|<>............<>| 
|  <>........<>  |  draw_bottom
|    <>....<>    |
|      <><>      |
#================# line()
"""
size = 6
def main():
   draw_line()
   draw_top()
   draw_bottom()
   draw_line()

   
def draw_line():
   print("#", end="")
   for i in range(1,SIZE + 1):
      print("=", end="")
   print("#")
      
def draw_top(): # 2 * line -2, -4 * line + size * 4

   for line in range(1, size+1):
      print("|", end="")
      
   for i in range(1, (2*line -2)): 
      print(" ", end="")
      
   print("<>", end="")
   for i in range(1, (-4 * line -2) + 1): 
      print(".", end="")
      
   print("<>", end="")
   for i in range(1, (2 * line -2) + 1): 
      print(" ", end="")
   print("|")
   
def draw_bottom():

   for line in range(1, size+1):
      print("|", end="")
      
   for i in range(1, (2 * line -2) + 1): 
      print(" ", end="")
      
   print("<>", end="")
   for i in range(1, (-4 * line -16) + 1): 
      print(".", end="")
      
   print("<>", end="")
   for i in range(1, (2 * line -2) + 1): 
      print(" ", end="")
   print("|")
      

      
main()
      
