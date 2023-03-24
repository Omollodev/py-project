def add(x, y):
    answer = x + y
    print(f"{x} + {y} = {answer} " '\n')


def substraction(x, y):
    answer = x - y
    print(f"{x} - {y} = {answer}" '\n')


def multiply(x, y):
    answer = x * y
    print(f"{x} * {y} = {answer}" '\n')


def floor_division(x, y):
    answer = x / y
    print(f"{x} / {y} = {answer}" "\n")


def module(x, y):
    answer = x % y
    print(f"{x} % {y} = {answer}" "\n")


def division(x, y):
    answer = x // y
    print(f"{x} // {y} = {answer}")


while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multipcation")
    print("D. Floor Division")
    print("E. Module")
    print("F. Divison")
    print("G.Exit")

    choice = input("Input your choice: ")

    if choice == "a" or choice == "A":
        print("Addition")
        x = int(input("Enter your first number: "))
        y = int(input("Enter a second number: "))
        add(x, y)
    elif choice == "b" or choice == "B":
        print("Substraction")
        x = int(input("Enter your first number: "))
        y = int(input("Enter a second number: "))
        substraction(x, y)
    elif choice == "c" or choice == "C":
        print("Multiplication")
        x = int(input("Enter your first number: "))
        y = int(input("Enter a second number: "))
        multiply(x, y)
    elif choice == "d" or choice == "D":
        print("Floor Divison")
        x = int(input("Enter your first number: "))
        y = int(input("Enter a second number: "))
        floor_division(x, y)
    elif choice == "e" or choice == "E":
        print("Reaminder")
        x = int(input("Enter your first number: "))
        y = int(input("Enter a second number: "))
        module(x, y)
    elif choice == "f" or choice == "F":
        print("Division")
        x = int(input("Enter your first number: "))
        y = int(input("Enter a second number: "))
        division(x, y)
    elif choice == "g" or choice == "G":
        print("Program termminated")
        quit()
