def main():
    n = int(input(f"how many names?\n"))
    longest_name(n)

def longest_name(n):
    long_name="a"

    for i in range(1,n+1):
        name = input(str("name #{i}?"))
        name = name.lower()
        print()
        name_length = len(name)

        if name_length > len(long_name):
            long_name = name
    print(long_name.title() + "'s name is longest")

main()