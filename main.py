# Alfred Brewer's main.py file

def encoder(code):
    result = ""

    for x in str(code):
        if int(x) < 7:
            result += str(int(x) + 3)
        else:
            result += str((int(x) - 7))

    return int(result)

def decoder(code):
    decoded_password = ""
    for digit in str(code):
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_password += decoded_digit
    return decoded_password

if __name__ == "__main__":
    while True:

        print("""
Menu
-------------
1. Encode
2. Decode
3. Quit
""")

        option = int(input("Please enter an option: "))
        original = ""

        if option == 1:
            stored = encoder(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")
        elif option == 2:
            print(f"The encoded password is {stored}, and the original password is {decoder(stored)}.")
        else:
            break



