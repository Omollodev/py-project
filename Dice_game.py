import random


def roll_dice():

    dice_drawing = {
        1: (
            "┌─────────┐",
            "│    1    │",
            "│    ●    │",
            "│         │",
            "└─────────┘",
        ),
        2: (
            "┌─────────┐",
            "│  ●      │",
            "│    2    │",
            "│      ●  │",
            "└─────────┘",
        ),
        3: (
            "┌─────────┐",
            "│  ● 3    │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘",
        ),
        4: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│    4    │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
        5: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ● 5 ●  │",
            "└─────────┘",
        ),
        6: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│  ● 6 ●  │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
    }

    roll = input("Roll the dice? (Yes/No): ")

    while roll.lower() == "Yes".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("dice rolled:{} and {} ".format(dice1, dice2))

        roll = input("Roll again? (Yes/No): ")
        print('\n'.join(dice_drawing[dice1]))
        print('\n'.join(dice_drawing[dice2]))


roll_dice()
