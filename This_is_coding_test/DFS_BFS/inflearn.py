
# 재귀함수를 이용한 이진수 출력
# 컴퓨터의 내부에서 재귀 함수의 수행은 스택 자료구조를 이용한다
# 가장 마지막에 호출한 함수가 먼저 수행을 끝내야 그 앞의 함수 호출이 종료되기 때문
# 스택 자료구조를 활용해야 하는 상당수 알고리즘은 재귀 함수를 이용해 간편하게 구현될 수 있음
# https://velog.io/@myway00/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-050-%EC%88%98%EC%97%B4-%EC%B6%94%EC%B8%A1%ED%95%98%EA%B8%B0%EC%88%9C%EC%97%B4-%ED%8C%8C%EC%8A%A4%EC%B9%BC-%EC%9D%91%EC%9A%A9

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

print('44. 부분 집합 구하기')
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


print('45합이같은 부분집합')
n = 6
s = [1,3,5,6,7,10]
v = [0]*6
flag =False
import sys
def bubun_45(x):
    global flag
    if flag==True:  # 하나 얻어걸리면 거기서 멈춤
        return
    if x==n:
        s_1 = []
        s_2 = []
        for i in range(n):
            if v[i]== 0:
                s_1.append(s[i])
            else:
                s_2.append(s[i])
        if sum(s_1)==sum(s_2):
            flag = True

        # print(' '.join(map(str,s_1)),' ',' '.join(map(str,s_2)))

    else:
        v[x]=1
        bubun_45(x+1)
        v[x]=0
        bubun_45(x+1)

bubun_45(0)
if flag==True:
    print('YES')
else:
    print('No')

print('46바둑이승차')
c = 259
n = 5
bag = [81,58,42,33,61]
sum = 0

def ba(x,sum):
    if x==n:
        if sum>c :
            print(sum)
            return

    else:
        ba(x+1,sum+bag[x])
        ba(x+1,sum)
ba(0,sum)
sum = 0
def ba_sol(L,sum):
    global result
    if sum>c:
        # print('over')  # 넘으면 계산 안하고 넘어감 아래꺼를 안한다 뿐이지, 다른 경우의 수 탐색을 종료하겠다는 뜻은 아님.
        return
    if L==n:
        # print(sum)
        if sum>result:   # sum은 재귀이기 때문에 다 들어가고, 모든 경우를 탐색함에 있어서 result를 갱신해주면서 확인한다.
            result = sum
    else:
        ba_sol(L + 1, sum + bag[L])
        ba_sol(L+1,sum)  # 순서 상관 없는 듯? 시간을 빨리 하고 싶으면 최댓값이기 때문에 반대로 해누는게 좋읗듯?
# 부분합 구하기 아직 안풀음
result = -3399
ba_sol(0,0)
print(result)

print('47 중복 순열 구하기')
n = 3
n = [i+1 for i in range(n)]
m =2
result=[0]*m
n_case = 0
def permutation_of_repetition(L):
    global n_case
    if L ==m:
        n_case+=1
        print(' '.join(map(str,result)))
        return
    else:
        for i in range(len(n)):
            result[L] = n[i]
            permutation_of_repetition(L+1)
permutation_of_repetition(0)
print(n_case)

# print('48 동전교환')
# n = 3
# bag_coin  =[1,2,5]
# bag_coin.sort(reverse = True)
#
# m = 15
# result = 0
# s = []
# def coin_exchange(L,sum,s):
#     if sum>15:
#         return
#     if sum==15:
#         print(s)
#
#
#         result
#
#
#     else:
#
#         coin_exchange(L+1,sum+,s)
#
# max_n = 10000
# coin_exchange()
print('49 순열구하기')
n = 3
m = 2
v = [0]*n
s = []
sum = 0
def permutation(L):
    global sum
    if L==m:
        sum +=1
        print(' '.join(map(str,s)))
    else:
        for i in range(n):
            if v[i]==1:
                continue
            else:
                v[i]=1
                s.append(i+1)
                permutation(L+1)
                v[i]=0
                s.pop()
permutation(0)
print(sum)

print('50 수열 추측하기_솔루션 공부할 것')
n = 4
f = 16
v = [0]*n
s=[]
re = 0
import copy
def pascal(s,n):
    s = copy.deepcopy(s)
    global re
    if len(s)==1:
        # print(s[0])
        re = s[0]
    else:
        a = []
        for i in range(n-1):
            a.append(s[i]+s[i+1])
        pascal(a,n-1)
        return
# pascal([3,1,2,4],4)
bag_s = []
def guess(L): #내풀이. 아직 솔루션 해결 안함
    global a
    global re
    global bag_s
    if re ==16:
        return
    if L==n:
        # print(' '.join(map(str,s)))
        pascal(s,n)
        if re==16:
            print(' '.join(map(str,s)))
            # return


    else:
        for i in range(n):
           if v[i]==1:
               continue
           else:
               v[i]=1
               s.append(i+1)
               guess(L+1)
               v[i]=0
               s.pop()
guess(0)

print('51 조합 구하기')
n = 4
r = 2
s = []
result = 0
def combi(L,B):
    global result
    if L==r:
        result+=1
        print(' '.join(map(str,s)))
    else:
        for i in range(B,n):
            s.append(i+1)
            combi(L+1,i+1)
            s.pop()

combi(0,0)
print(result)

print('51 조합 구하기(중복?)')
n = 4
r = 2
s = []
result = 0
def combi(L,B):
    global result
    if L==r:
        result+=1
        print(' '.join(map(str,s)))
    else:
        for i in range(0,n):
            s.append(i+1)
            combi(L+1,i+1)
            s.pop()

combi(0,0)
print(result)

print('52 수들의 조합')
# N개의 정수가 주어지면 그 숫자들 중 K개를 뽑는 조합의 합이 임의의 정수 M의 배수인 개수
# 는 몇 개가 있는지 출력하는 프로그램을 작성하세요.
# 예를 들면 5개의 숫자 2 4 5 8 12가 주어지고, 3개를 뽑은 조합의 합이 6의 배수인 조합을
# 찾으면 4+8+12 2+4+12로 2가지가 있습니다.
n = 5
k = 3
v = [2,4,5,8,12]
m = 6
cnt = 0
s = []
del sum
def combi_52(L,B):
    global m
    global cnt
    if L==k:
        if sum(s)%m ==0:
            print(s)
            cnt+=1
    else:
        for i in range(B,n):
            s.append(v[i])
            combi_52(L+1,i+1)
            s.pop()
combi_52(0,0)
print(cnt)

print('53 인접행렬 가중치 방향그래프')
# n = 6
# m = 9
# g = [[0]*(n) for _ in range(n)]
# print(g)
# for _ in range(m):
#     x,y,c = map(int,input().split())
#     g[x-1][y-1] = c
# for i in range(n):
#     print(' '.join(map(str,g[i])))

print('54 경로탐색 (DFS 그래프)_한번 더 풀어볼 것')
# 방향그래프가 주어지면 1번 정점에서 n번 정점으로 가는 모든 경로의 가지 수를 출력하는 프로그램을 작성하세요.
n = 5
m = 9
g = [[0,0,0,0,0,0],
    [0,0, 1, 1, 1, 0],
     [0,1, 0, 1, 0, 1],
     [0,0, 0, 0, 1, 0],
     [0,0, 1, 0, 0, 1],
     [0,0, 0, 0, 0, 0]]
v = [[0,0,0,0,0,0],
     [0,0,0,0,0,0],
     [0,0,0,0,0,0],
     [0,0,0,0,0,0],
     [0,0,0,0,0,0],
     [0,0,0,0,0,0]]
s = []
cnt = 0
def dfs_54(c):
    global cnt
    if c == 5:
        print('지나온 길 출력')
        s.append(c)
        print(s)
        cnt+=1
    else:
        s.append(c)
        print(c)
        for i in range(1,n+1):
            if g[c][i]==1 and v[c][i]==0 and v[i][c]==0:
                v[c]=[1]*(n+1)
                v[i][c] = 1
                dfs_54(i)
                v[c] = [0]*(n+1)
                v[i][c] = 0
                s.pop()

dfs(1)
print('cnt = ',cnt)



print('55 최대점수 구하기 (DFS)')
n = 5
m = 20
g = [(10, 5), (25, 12), (15, 8), (6, 3), (7, 4)]
t = 0  #시간
s = 0   # score
tmp = []
ch = [0]*(n)
# print(g[0][1])
# q,w = g[-1]
# print(q,w)
max_s = -11
def dfs_55():
    global s
    global t
    global max_s
    if t>=m:
        # print(tmp)
        if t>m:
            tmp_s,tmp_t =tmp[-1]
            print(s-tmp_s,t-tmp_t)
            max_s = max(max_s,s-tmp_s)
        else:
            print(s,t)
            max_s = max(max_s, s)
    else:
        for i in range(n):
            if ch[i]==0:
                ch[i]=1
                tmp.append(g[i])
                s+=g[i][0]
                t+=g[i][1]
                dfs_55()
                ch[i]=0
                s -= g[i][0]
                t -= g[i][1]
                tmp.pop()
dfs_55()
print(max_s)


def DFS_sol(x,s,time) :
    global res
    if time>m :
        return
    if x==n :
        if s>res:
            res=s
    else : #두가지 경우로 나뉜다. 문제를 푸는 경우와 풀지 않는 경우
        DFS_sol(x+1, s+pv[x] , time+pt[x])
        DFS_sol(x+1, s, time)
if __name__=='__main__' :
    n, m = map(int, input().split())
    pv =list()
    pt=list()
    for i in range(n) :
        a,b = map(int, input().split())
        pv.append(a)
        pt.append(b)
    res=-1
    DFS(0,0,0)
    print(res)