import random

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
letters_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letters_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_']

print("Welcome to the Password Generator")
firstin = input("Do you want to choose the length of the password or would you like it to be random [ch/ran]")

if firstin.lower() == 'ch':
    try:
        length = int(input("How long would you like the password to be?"))
    except ValueError:
        print("Invalid Error")
elif firstin.lower() == "ran":
    length = random.random(20)