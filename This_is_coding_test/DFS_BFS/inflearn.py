# 재귀함수를 이용한 이진수 출력
# 컴퓨터의 내부에서 재귀 함수의 수행은 스택 자료구조를 이용한다
# 가장 마지막에 호출한 함수가 먼저 수행을 끝내야 그 앞의 함수 호출이 종료되기 때문
# 스택 자료구조를 활용해야 하는 상당수 알고리즘은 재귀 함수를 이용해 간편하게 구현될 수 있음



a = 11
s=[]
def binary(num):
    if num==0:
        return
    else:
        binary(num//2)
        print(num%2,end='')
binary(a)
print()
print(s)
# for i in range(5):
#     print(a % 2)
#     a = a//2
print()
n = 5
s=[]
def fac(n):
    if n==0:
        return
    else:  # print 위치에 따라서, 위에서 프린트 하면 5부터 출력. 아래서 프린트 하면 1부터 출력
        # print(n,end = '')
        s.append(n)
        fac(n-1)
        print(n, end='')
fac(n)
print()
print(s)
# 일반적으로 모든 경우의 수를 탐색할 때는 반복문을 사용하지만, 한 가지
# 경우의 수에서 두 가지 이상의 상황으로 분화될 경우에는 재귀함수를 통해 탐색해야 한다

# 백트래킹: 모든 경우의 수를 고려하는 알고리즘으로, 모든 가능한 케이스가 나열된 상태공간트리를
# 작성해서 문제를 푼다. 백트래킹의 종류로 DFS/BFS가 있으며 모든 경우의 수를 구해야 할 때는 DFS,
# 최단거리를 구할 때는 BFS를 사용해서 문제를 푼다.

print('부분 집합 구하기')
n = 3
s = [i+1 for i in range(3)]
print(s)
def bubun(x):
    if x==n:
        for i in range(n):
            if ch[i]==1:
                print(s[i],end=' ')
        print()
        return
    else:
        ch[x] = 1
        bubun(x+1)
        ch[x] = 0
        bubun(x+1)

ch = [0]*(n)
bubun(0)

