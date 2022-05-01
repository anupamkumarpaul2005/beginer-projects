import  re

print("""
          Calculator
    
    This cakculator can solve simple equations with functions with denotation:
    + : Addition            - : Subtraction            * : Multiplication
    / : Division            ^ : Exponent                ! : Factorial
    (): Parentheses         % : Percentage
    Having any other characters other than these would result in error.
    Type 'Quit' to exit.
""")


while True:
    query=input().lower()
    if query=="quit":
        exit()
    flag=False
    for n in query:
        if n not in ".1234567890+-*/^!()%":
            flag = True
    if flag:
        print("Wrong input!")
        continue
    expression = re.split('+|-|*|/|',query)
    print(expression)