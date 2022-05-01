import random

print("""
                PASWORD GENERATOR
                
        This will help you generate a password of any length.
        
        To Start, type 'Generate'
        To Change Settings, type 'Settings'
        To quit, type 'Quit'
        
""")
data = [n for n in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTVWXYZ01234567890!@#$%^&*()?.,:"]


def gen():
    print("Enter length of password: ")
    l = int(input())
    pswrd = "".join(random.sample(data, l))
    print("Your password can be: "+pswrd)


def settings():
    print("""
            Upper Case Alphabets:   YES                          Lower Case Alphabets: YES
            Numbers:                YES                          Special Characters:   !@#$%^&*()?.,:
    """)
    print("You want to add  or remove ")


while True:
    query = input().upper()
    if query == 'QUIT' or query == 'Q':
        exit()
    elif query == 'GENERATE' or query == 'G':
        gen()
    else:
        print("Not a valid request.")
