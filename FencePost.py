def print_letters(word):
   for i in range(0, len(word)-1): #0 , 1
      print(word[i], end="") #post
      print(", ", end="") #wird
      
   print(word[-1], end="")


def print_letters_1(word):
    print(word[0], end="")  

    for i in range(1, len(word)):
        print(", ", end="")  
        print(word[i], end="")

print_letters_1("abc")
