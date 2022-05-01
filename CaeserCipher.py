print("""
        CAESER CIPHER
        
    
    To encode, type 'Encode'
    To quit, type 'Quit'

""")


upper_case=list(n for n in "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
lower_case=list(n for n in "abcdefghijklmnopqrstuvwxyz")
while True:
    query = input().upper()
    if query == 'QUIT' or query == 'Q':
        print("Visit Again!")
        exit()
    elif query == 'ENCODE' or query == 'E':
        msg = input("Enter the message:\n")
        sft= int(input("Enter the shift:\n"))
        code=""
        for n in msg:
            if n in lower_case:
                code+=lower_case[(lower_case.index(n)+sft)%26]
            elif n in upper_case:
                code+=upper_case[(upper_case.index(n)+sft)%26]
            else:
                code+=n
        print("The encoded message will be: "+code)
    elif query=='DECODE' or query=='D':
        msg = input("Enter the message:\n")
        sft = int(input("Enter the shift:\n"))
        code = ""
        for n in msg:
            if n in lower_case:
                code += lower_case[(lower_case.index(n) - sft) % 26]
            elif n in upper_case:
                code += upper_case[(upper_case.index(n) - sft) % 26]
            else:
                code += n
        print("The decoded message will be: " + code)
    else:
        print("Not a valid request.")