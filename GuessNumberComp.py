import random
import time

print("""
          Let me guess your Number
          
    User will input a number (integer) between 1 and 1000. Computer will try to guess the number. Each wrong guess 
    will give a hint of the guess being less or more. Let's see how good the computer guesses your number.
    
    Type 'Play' to start the game and play it again.
    Type 'Quit' to exit the game.
    
""")

while True:
    query = input().upper()
    if query == 'QUIT' or query == 'Q':
        exit()
    elif query == 'PLAY' or query == 'P':
        print("Enter your number:")
        while True:
            num = int(input())
            if 1 <= num <= 1000:
                break
            else:
                print("Enter a number between 1 and 10000.")
        numGuess = 1
        start = 1
        end = 1000
        while True:
            time.sleep(1)
            print(f"Round {numGuess}:")
            guess = random.randint(start, end)
            print(f"Computer guessed: {guess}")
            if guess > num:
                print("To Computer: 'Guess is high'.")
                end = guess - 1
            elif guess == num:
                print(f"Computer guessed correct on guess {numGuess}")
                break
            else:
                print("To Computer: 'Guess is small'.")
                start = guess + 1
            numGuess += 1
    else:
        print("Invalid request.")
