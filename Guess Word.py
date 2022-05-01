import requests

print("""\
           Guess the Word (HangMan)
           
     Enter a single letter to check if a letter is present.
     You will get 7 guess. you will get 1 more guess in case you guess correct.
""")
while True:
    while True:
        response = requests.get("https://random-word-api.herokuapp.com/word?swear=0")
        word = response.json()[0]
        if len(word) <= 7:
            break
    length = len(word)
    word = str.upper(word)
    print(word)
    word = [i for i in word]
    encodedWord = ["_" for i in word]
    tries = 1
    while True:
        print("".join(encodedWord))
        print("Enter your guess:")
        while True:
            guess = input().upper()
            if len(guess) > 1:
                print("You are allowed to input a single letter. Try again!")
            else:
                break
        if guess in word:
            c = 0
            for i in word:
                if i == guess:
                    encodedWord[c] = guess
                c += 1
            print(f"Guess left: {7 - tries}.")
        else:
            print(f"Wrong! Guess left: {7 - tries}.")
            tries += 1
        if encodedWord == word:
            print(f"Congratulations! You won!")
            break
        elif tries == 7:
            print("You Lose!")
            break
    print("Wanna play again?(y/n)")
    while True:
        query = input().lower()
        if query == 'y' or query == 'n':
            break
        print("Invalid. Type again.")
    if query == 'n':
        exit()
