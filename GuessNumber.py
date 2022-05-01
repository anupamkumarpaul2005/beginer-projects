import sys
import random

print("""\
         Guess the Number

    Some hints will be given. Guess the number now. :)
    
    To START, type 'START' 
    To QUIT, type 'QUIT'
""")
acceptable_keys = ['START', 'QUIT']
while True:
    user = input().upper()
    if user in acceptable_keys:
        break
    print("Try Again!")
if user == acceptable_keys[1]:
    sys.exit("Thank You! Visit again.")


def divisible(n):
    r = random.randint(1, 10)
    if n % r == 0:
        print(f"The number is divisibile by {r}.")
    else:
        print(f"The number is not divisibile by {r}.")


def multiple(n):
    r = random.randint(3, 10)
    print(f"{n * r} is a multiple of the number")


def prime(n):
    f = 0
    for i in range(1, n + 1):
        if n % i == 0:
            f += 0
    if f == 2:
        print("The number is prime.")
    else:
        print("The number is not prime.")


def lesserOrGreater(n, g):
    if n > g:
        print("You guess is less!")
    else:
        print("Your guess is high!")


num = random.randint(1, 100)
c = 0
while True:
    guess = 0
    if c > 0:
        hint = random.randint(1, 3)
    else:
        hint = random.randint(1, 2)
    print("Hint:")
    if c == 4:
        prime(num)
    elif hint == 1:
        divisible(num)
    elif hint == 2:
        multiple(num)
    elif hint == 3:
        lesserOrGreater(num, guess)

    print("Enter your guess:")
    guess = int(input())
    if guess == num:
        print(f"You won on try {c + 1}")
        break
    else:
        print(f"Guess left {10 - c - 1}")
        if c == 9:
            break
    c += 1
