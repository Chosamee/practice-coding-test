def  p14719():
    # O(n^2)
    H, W = map(int, input().split())
    hList = list(map(int, input().split()))
    
    check = 1
    water = 0
    while True:
        start = -1

        for i in range(len(hList)):
            if check <= hList[i]:
                if start != -1:
                    water += (i - start - 1)
                start = i
        if start == -1:
            break
        check += 1
    print(water)


def p14719g():
    # O(n)
    print()



if __name__ == "__main__":
    p14719()