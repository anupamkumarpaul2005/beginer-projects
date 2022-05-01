print("Enter an even number:")
n=int(int(input())/2)
for i in range(1,n+1):
    for j in range(2):
        print("\t"*(n-i)+"*\t"*(i*2)+"\t"*(n-i))