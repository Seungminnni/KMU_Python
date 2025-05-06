def main():
    tower1()
    tower2()
    tower3()

def tower1():
    top_of_tower()
    long_part_of_tower()
    short_part_of_tower()
    long_part_of_tower()
    print()
    
def tower2():
    top_of_tower()
    long_part_of_tower()
    short_part_of_tower()
    print()
    
def tower3():
    top_of_tower()
    short_part_of_tower()
    print()
    
def top_of_tower():
    print("  *")
    print(" ***")
    print("*****")
    
def short_part_of_tower():
    print(" ###")
    print(" ###")
    
def long_part_of_tower():
    print("-----")
    print("-----")
    
main()