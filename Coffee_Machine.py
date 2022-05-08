print("""
            Welcome to the Coder's Cafe

        There are 3 flavours:
        - Espresso (Requires 50mL water and 18g coffee)                     $1.50
        - Latte (Requires 200mL of water, 24g coffee and 150mL milk)        $2.50
        - Cappuccino (Requires 250mL of water, 24g coffee and 100mL milk)   $3.00
        
        
        To get report on current resources, type 'Resource'
        To get your favourite coffee, type 'Coffee'
        If you want to stop at any moment, type 'Quit'
        
""")


def resource():
    print("Resources:")
    for items in resources:
        print(f"{items}:\t{resources[items]}")
    print(f"Money:\t{money}")


def check_resource():
    if not (ingredient["Water"] <= resources["Water"] and ingredient["Coffee"] <= resources["Coffee"] and
            ingredient["Milk"] <= resources["Milk"]):
        return True
    return False


resources = {"Water": 25000, "Milk": 10000, "Coffee": 1000}
money = 0
menu = {"espresso": {"Water": 50, "Coffee": 18, "Milk": 0, "price": 150},
        "latte": {"Water": 200, "Coffee": 24, "Milk": 150, "price": 250},
        "cappuccino": {"Water": 250, "Coffee": 24, "Milk": 100, "price": 300}}
while True:
    query = input().upper()
    if query == "COFFEE" or query == 'C':
        coffee_type = input("What do you want to order? (Espresso, Latte or Cappuccino)\n").lower()
        ingredient = menu[coffee_type]
        if check_resource():
            print("Not enough resources left.")
            continue
        user_money = int(input("Enter the money(in dollars):\n")) * 100
        coffee_money = menu[coffee_type]["price"]
        if user_money < coffee_money:
            print("Not enough money has been given. Your money is being returned.")
            continue
        elif user_money > coffee_money:
            print("${:.2f} is being returned.".format((user_money - coffee_money) / 100))
        money += coffee_money
        for item in resources:
            resources[item] -= ingredient[item]
        print("Here's your coffee!")
    elif query == "RESOURCE" or query == 'R':
        resource()
    elif query == "QUIT" or query == 'Q':
        quit()
    else:
        print("Not a valid request.")
