def p16916():
    S = list(map(str, input()))
    P = list(map(str, input()))
    table = [0 for _ in range(len(S))]
    pLen = len(P)
    i = 0
    for j in range(1, pLen):
        while i > 0 and P[i] != P[j]:
            i = table[i-1]
        if P[i] == P[j]:
            i += 1
            table[j] = i

    i = 0
    for j in range(len(S)):
        while i > 0 and P[i] != S[j]:
            i = table[i-1]
        if P[i] == S[j]:
            i += 1
            if i == pLen:
                return True
    return False

if __name__ == "__main__":
    print(int(p16916()))