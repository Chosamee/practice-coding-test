from collections import *

def p13460():
    N, M = map(int, input().split())
    MAP = []
    for row in range(N):
        MAP.append(list(map(str,input())))
        for col in range(M):
            if MAP[row][col] == "R":
                rx, ry = row, col
            elif MAP[row][col] == "B":
                bx, by = row, col
            elif MAP[row][col] == "O":
                ox, oy = row, col
    
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = deque()
    cnt = 0
    visited = []
    visited.append((rx, ry, bx, by))
    q.append((rx, ry, bx, by, cnt))

    while q:
        rx, ry, bx, by, cnt = q.popleft()

        if cnt >= 10:
            return -1

        for dx, dy in d:
            nrx, nry, nbx, nby, ncnt = rx, ry, bx, by, cnt
            rDist = 0
            while MAP[nrx + dx][nry + dy] != '#' and MAP[nrx][nry] != 'O':
                nrx += dx
                nry += dy
                rDist += 1

            bDist = 0
            while MAP[nbx + dx][nby + dy] != '#' and MAP[nbx][nby] != 'O':
                nbx += dx
                nby += dy
                bDist += 1

            if MAP[nbx][nby] != 'O':
                if nrx == ox and nry == oy:
                    return ncnt + 1
                if nrx == nbx and nry == nby:
                    if rDist > bDist:
                        nrx, nry = nrx - dx, nry - dy
                    else:
                        nbx, nby = nbx - dx, nby - dy
                if (nrx, nry, nbx, nby) not in visited:
                    ncnt += 1
                    q.append((nrx, nry, nbx, nby, ncnt))
                    visited.append((nrx, nry, nbx, nby))
                    
    return -1


if __name__ == "__main__":
    print(p13460())
