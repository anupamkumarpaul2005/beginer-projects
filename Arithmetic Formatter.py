def arithmetic_arrangement(l, bool=False):
    exp = [i for i in l]
    operand1 = []
    operator = []
    operand2 = []
    maxlen = []
    for i in exp:
        key = []
        n = ""
        for j in i:
            if j in "1234567890":
                n += j
            else:
                key.append(n)
                key.append(j)
                n = ""
        key.append(n)
        l1, l2 = len(key[0]), len(key[2])
        mn = 0 if l1 < l2 else 2
        key[mn] = " " * (abs(l1 - l2)) + key[mn]
        operand1.append(key[0])
        operator.append(key[1])
        operand2.append(key[2])
        maxlen.append(len(key[0]))
    print(" " + "\t ".join(operand1))
    line = []
    for a, b in zip(operator, operand2):
        line.append(a + b)
    print("\t".join(line))
    for i in maxlen:
        print("-" * (i + 1), end="\t")
    print()
    if bool:
        res = []
        for a, b, c in zip(operand1, operator, operand2):
            if b == "+":
                result = str(int(a) + int(c))
            else:
                result = str(int(a) - int(c))
            result = " " * (len(c) + 1 - len(result)) + result
            res.append(result)
        print("\t".join(res))


question = ["9000+10", "999+999", "52+5689", "1634-891", "50-389", "0-23"]
arithmetic_arrangement(question, True)
