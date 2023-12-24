import string
import random
from cryptography.fernet import Fernet


def generate_random_password():
    global final_password
    characters = list(string.ascii_letters + string.digits + string.punctuation)
    # print("Characters :  ", characters)
    length = int(input("Enter the length of password : "))
    random.shuffle(characters)
    # print("suffled Characters :  ", characters)
    password = []
    for i in range(length):
        password.append(random.choice(characters))
    random.shuffle(password)
    final_password = ("".join(password))
    # print("Final Password :  ", final_password)


def encrypt(key, message):
    alpha = string.ascii_letters
    result = ""

    for letter in message:
        if letter in alpha:
            letter_index = (alpha.find(letter) + key) % len(alpha)
            # print(letter_index)
            result = result + alpha[letter_index]
            # print(f"Aplha : {result}")
        else:
            result = result + letter

    return result


def decrypt(key, message):
    alpha = string.ascii_letters
    result = ""

    for letter in message:
        if letter in alpha:
            letter_index = (alpha.find(letter) - key) % len(alpha)
            # print(letter_index)
            result = result + alpha[letter_index]
            # print(f"Aplha : {result}")
        else:
            result = result + letter

    return result


def main():
    a = int(input("Do you want to save (1) or do you want to fetch (2) passwrd"))
    if a == 1:
        platform = input("Platform : ")
        generate_random_password()
        # print(final_password)

        enc = encrypt(11, f"{platform} --> {final_password}")

        file = open("password.txt","a")
        file.write(f"{enc}\n")
        file.close()
    else:
        file = open("password.txt", "r")
        content = file.read()
        dec = decrypt(11, content)
        print(dec)
        file.close()


main()