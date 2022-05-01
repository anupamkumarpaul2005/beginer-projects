import random
import time

print("""
            Rock Paper Scissor
        
    Lets play Rock Paper and Scissor of 10 rounds. You can either play against computer or pVp.Enjoy :)
    
    Rules:
    1. Rock breaks Scissors.
    2. Paper blocks Rock.
    3. Scissor cuts Paper.
    
    Denotation: 'R':Rock
                'P':Paper
                'S':Scissor
    Type 'Play' to start.
    Type 'Quit' to exit.
    
""")

choices = ['R', 'P', 'S']


def winner(a, b):
    if (a == 'R' and b == 'S') or (a == 'P' and b == 'R') or (a == 'S' and b == 'P'):
        return 1
    elif a == b:
        return 0
    else:
        return -1


def computer():
    plays = 1
    p = 0
    c = 0
    d = 0
    while plays <= 10:
        print(f"Round {plays}")
        print("Enter your choice:")
        while True:
            pl = input().upper()
            if pl in choices:
                break
            print("Invalid Input. Enter your choice:")
        comp = random.choice(choices)
        print(f"Computer chose: {comp}")
        result = winner(pl, comp)
        if result == 1:
            print("Player won.")
            p += 1
        elif result == -1:
            print("Computer won.")
            c += 1
        else:
            print("It's a draw.")
            d += 1
        plays += 1
        time.sleep(0.5)
    print(f"Player: {p}\nComputer: {c}\nDraws: {d}")
    if p > c:
        print("Congratulations! Player won.")
    elif p < c:
        print("Sorry! You lose.")
    else:
        print("It's a draw.")


def player():
    plays = 1
    p1 = 0
    p2 = 0
    d = 0
    while plays <= 10:
        print(f"Round {plays}")
        print("Player 1:")
        while True:
            pl1 = input().upper()
            if pl1 in choices:
                break
            print("Invalid Input. Enter your choice:")
        print("Player 2:")
        while True:
            pl2 = input().upper()
            if pl2 in choices:
                break
            print("Invalid Input. Enter your choice:")
        result = winner(pl1, pl2)
        if result == 1:
            print("Player 1 won.")
            p1 += 1
        elif result == -1:
            print("Player 2 won.")
            p2 += 1
        else:
            print("It's a draw.")
            d += 1
        plays += 1
        time.sleep(0.5)
    print(f"Player 1: {p1}\nPlayer 2: {p2}\nDraws: {d}")
    if p1 > p2:
        print("Congratulation! Player 1 won.")
    elif p1 < p2:
        print("Congratulation! Player 2 won.")
    else:
        print("It's a draw.")


while True:
    query = input().upper()
    if query == 'QUIT' or query == 'Q':
        break
    elif query == 'PLAY' or query == 'P':
        print("Play against computer('C') or against another player('P'):")
        while True:
            query = input().upper()
            if query == 'C':
                computer()
                break
            elif query == 'P':
                player()
                break
            else:
                print("Invalid Input!")
    else:
        print("Invalid Input!")
