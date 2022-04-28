import time
import random

print("""\
            Roll the Dice
            
    Type 'Roll' to roll again and again and again
    Type 'Quit' to exit


""")


# Dice GUI
def dice(n):
    if n == 1:
        print("|       |")
        print("|       |")
        print("|   *   |")
        print("|       |")
        print("|       |")
    elif n == 2:
        print("|       |")
        print("|  *    |")
        print("|       |")
        print("|    *  |")
        print("|       |")
    elif n == 3:
        print("|   *   |")
        print("|       |")
        print("|   *   |")
        print("|       |")
        print("|   *   |")
    elif n == 4:
        print("|       |")
        print("| *   * |")
        print("|       |")
        print("| *   * |")
        print("|       |")
    elif n == 5:
        print("|       |")
        print("| *   * |")
        print("|   *   |")
        print("| *   * |")
        print("|       |")
    elif n == 6:
        print("| *   * |")
        print("|       |")
        print("| *   * |")
        print("|       |")
        print("| *   * |")

    else:
        print("Error!")


while True:
    query = input().upper()
    if query == 'QUIT' or query == 'Q':
        exit()
    elif query == 'ROLL' or query == 'R':
        print("Dice is rolling...\n3...")
        time.sleep(0.5)
        print("2...")
        time.sleep(0.75)
        print("1...")
        time.sleep(0.5)
        print("You rolled: ")
        dice(random.randint(1, 6))

    else:
        print("Not a valid request!")
