def show_twos(n):
    print(f"{n} = ", end="")
    while n % 2 == 0:
        print("2 * ", end="")
        n= n // 2
    print(n)

