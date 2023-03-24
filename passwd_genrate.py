import string
import random

character = list(string.ascii_letters + string.digits + "!@#$%^&*()~`?")


def generate_password():
    password_length = int(
        input("How long would yu like your password to be? "))

    random.shuffle(character)

    password = []

    for x in range(password_length):
        password.append(random.choice(character))

    random.shuffle(password)

    password = "".join(password)

    print(password)


option = input("Do you want to generate a password ? (Yes/No): ")

if option == "Yes":
    generate_password()
elif option == "No":
    print("Program ended.")
    quit()
else:
    print("Invalid input, Please input Yes or No")
    quit()
