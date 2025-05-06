text = input("Your message? ")
key = int(input("Encoding key? "))
text = text.upper()


for letter in text:
    if "A" <= letter <= "Z":
        shifted_num = ord(letter) + key
        if shifted_num > ord("Z"):
            shifted_num = shifted_num % ord('[') + ord('A')
        print(chr(shifted_num), end="")
    else:
        print(letter, end="")



