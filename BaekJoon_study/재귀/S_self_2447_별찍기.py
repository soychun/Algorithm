import sys
n = int(sys.stdin.readline())
n=0
def p(n):
    if n==0:
        return '*'
def b(n):
    if n==0:
        return ' '
a = []
a.append([p(0)*3])
a.append([p(0)+b(0)+p(0)])
a.append([p(0)*3])
# https://imgzon.tistory.com/37