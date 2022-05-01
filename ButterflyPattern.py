n = int(input("Enter max length of each wing:\n"))
for i in range(1, n + 1):
    c = i * 2
    for j in range(1, i + 1):
        print("*", end="")
    for j in range(2 * n - c):
        print(" ", end="")
    for j in range(1, i + 1):
        print("*", end="")
    print()
for i in range(n, 0, -1):
    c = i * 2
    for j in range(1, i + 1):
        print("*", end="")
    for j in range(2 * n - c):
        print(" ", end="")
    for j in range(1, i + 1):
        print("*", end="")
    print()
