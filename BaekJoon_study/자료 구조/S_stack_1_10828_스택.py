def commend_(c,l):
    if c[0] == 'push':
        l.append(int(c[1]))
    elif c[0] == 'pop':
        if len(l) ==0:
            print(-1)
        else:
            print(l.pop())
    elif c[0] == 'size':
        print(len(l))
    elif c[0] == 'empty':
        if len(l) == 0:
            print(1)
        else:
            print(0)
    elif c[0] == 'top':
        if len(l) == 0:
            print(-1)
        else:
            print(l[-1])
    else:
        return
import sys
input = sys.stdin.readline
l = []
n = int(input())
for _ in range(n):
    c = input().rstrip().split()
    print(c)
    commend_(c,l)
