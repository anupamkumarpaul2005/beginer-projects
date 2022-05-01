import random

print("""
                    BLACKJACK CARD PLAY
                    
        To play, type Play
        To Quit, type Quit

        
        Player will have $1000 at first.
        
""")


def bust(player, dealer):
    if player > 21:
        return 1
    if dealer > 21:
        return 0
    return -1


def compare(player, dealer):
    if bust(player, dealer) == -1:
        if player > dealer:
            return 0
        elif dealer > player:
            return 1
        else:
            return -1
    return bust(player, dealer)


def bet():
    print("Enter the anount of bet:")
    while True:
        b = int(input())
        if b <= wallet:
            return b
        print("You do not have that much amount in your account.")
        continue


def points(l):
    score = 0
    for n in l:
        if n.isnumeric():
            score += int(n)
        if n.isalpha() and n != 'A':
            score += 10
    if 'A' in l:
        if 21 - score < 11:
            score += 1
        else:
            score += 11
    return score


def hit_or_stand():
    print("Will you hit or stand?(h/s)")
    while True:
        user = input().lower()
        if user == 'h':
            while True:
                p = random.choice(deck)
                if p not in pl:
                    break
            pl.append(p)
            if points(pl) > 21:
                return "Bust"
            pldeck = ", ".join(pl)
            print(f"You:     {pldeck}")
            return hit_or_stand()
        elif user == 's':
            return
        print("Not a valid request.")


deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
wallet = 1000
print(f"Wallet: {wallet}")
while True:
    query = input().upper()
    if query == 'QUIT' or query == 'Q':
        break
    elif query == 'PLAY' or query == 'P':
        bet_amount = bet()
        dl = random.sample(deck, k=2)
        pl = random.sample(deck, k=2)
        print(f"Dealer:  ?, {dl[1]}")
        print(f"You:     {pl[0]}, {pl[1]}")
        h = hit_or_stand()
        d_deck = ", ".join(dl)
        p_deck = ", ".join((pl))
        print(f"Dealer:  {d_deck}")
        print(f"You:     {p_deck}")
        if h == "Bust":
            wallet -= bet_amount
            print(f"Bust!\nYou lose ${bet_amount}.\nWallet: {wallet}")
            continue
        res = compare(points(pl), points(dl))
        if res == 0:
            wallet += bet_amount
            print(f"You Won!\nYou win ${bet_amount}.\nWallet: {wallet}")
        elif res == 1:
            wallet -= bet_amount
            print(f"Dealer Won!\nYou lose ${bet_amount}.\nWallet: {wallet}")
        else:
            print(f"Stand Off!\nWallet: {wallet}")
