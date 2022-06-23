from sympy import Max


def p12100():
    N = int(input())
    MAP = []
    for row in range(N):
        MAP.append(list(map(str,input())))

# pseudo
def dfs(MAP, cnt, max):
    if cnt >= 5:
        return MAP, cnt, max
    MAP1, cnt, max1 = dfs(move(MAP), cnt, max)
    MAP2, cnt, max2 = dfs(move(MAP), cnt, max)
    MAP3, cnt, max3 = dfs(move(MAP), cnt, max)
    MAP4, cnt, max4 = dfs(move(MAP), cnt, max)
    max = Max(max1, max2, max3, max4)
    max
    cnt += 1
    return MAP, cnt, max

def move(pos):
    print()


if __name__ == "__main__":
    print()