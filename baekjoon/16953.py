from collections import *

def p16953(): 
    A, B = map(int, input().split())
    cnt = 1
    while(A != B):
        if(A > B):
            cnt = -1
            break
        elif(B%2 == 0):
            B = B//2
            cnt += 1
        elif(B%10 == 1):
            B = B//10
            cnt += 1
        else:
            cnt = -1
            break
    print(cnt)

# use BFS
def p16953b():
    A, B = map(int, input().split())
    cnt = 1
    q = deque([(A, cnt)])
    while(q):
        a, c = q.popleft()
        if(a == B):
            print(c)
            return
        if(a * 2 <= B):
            q.append((a * 2, c + 1))
        if(a * 10 + 1 <= B):
            q.append((a * 10 + 1, c + 1))
    print(-1)
    

if __name__ == "__main__":
    p16953()
    # p16953b()