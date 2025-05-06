SIZE=3

def main():
    rocket()

def rocket():
    top_bottom()
    stack_layer()
    up_body()
    down_body()
    stack_layer()
    down_body()
    up_body()
    stack_layer()
    top_bottom()

def top_bottom():
    for i in range(2*SIZE-1):
        print(" "*((2*SIZE-1)-i), end="")
        print("/"*(i+1), end="")
        print("**", end="")
        print("\\"*(i+1))
def up_body():
    for j in range(SIZE):
        print("|", end="")
        print("."*(2-j), end="")
        print("/\\"*(j+1), end="")
        print("."*(4-(2*j)), end="")
        print("/\\"*(j+1), end="")
        print("."*(2-j), end="")
        print("|")
def down_body():
        for j in range(SIZE):
            print("|", end="")
            print("."*(j), end="")
            print("\\/"*(3-j), end="")
            print("."*(2*j), end="")
            print("\\/"*(3-j), end="")
            print("."*(j), end="")
            print("|")
def stack_layer():
    print("+")

main()





