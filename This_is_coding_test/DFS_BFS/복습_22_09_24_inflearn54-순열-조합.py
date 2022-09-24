# inflearn 54 경로 구하기

n = 5
m = 9
ch=[0]*(n+1)  # 한번만 거치기 때문에
cnt = 0 #경우의 수 세기
# g = [[0]*(n+1) for _ in range(n+1)]
# print(g)
# for i in range(m):
#     a,b = map(int,input().split())
#     g[a][b] = 1
# print(g)

g = [[0, 0, 0, 0, 0, 0],
     [0, 0, 1, 1, 1, 0],
     [0, 1, 0, 1, 0, 1],
     [0, 0, 0, 0, 1, 0],
     [0, 0, 1, 0, 0, 1],
     [0, 0, 0, 0, 0, 0]]

s = []
s.append(1)
ch[1] = 1

def dfs_search(c): #순열이랑 같은 맥락인 것.
    global cnt
    if  c == 5:
        print(s)
        cnt += 1
        # 종료조건
    else:
        for i in range(n+1):
            if g[c][i]==1 and ch[i]==0:
                ch[i]=1
                s.append(i)
                dfs_search(i)
                ch[i]=0
                s.pop()


dfs_search(1)
print(cnt)


# inflearn 54 순열 구하기
n = 3
m = 2
s = []
ch = [0]*(n)
cnt = 0
def permutation(L):
    global cnt
    if L==m:
        cnt+=1
        print(' '.join(map(str,s)))
    else:
        for i in range(n):
            if ch[i]==0:
                ch[i] = 1
                s.append(i+1)
                permutation(L+1)
                s.pop()
                ch[i]=0

permutation(0)
print(cnt)

n = 4
r = 2
s =[]
cnt =0

def combination(L,B):
    global cnt
    if L==r:
        print(' '.join(map(str,s)))
        cnt+=1
    else:
        for i in range(B,n):
            s.append(i+1)
            combination(L+1,i+1)
            s.pop()

combination(0,0)
print(cnt)

# 순열은 check가 필요하고, 조합은 check 배열이 필요하지 않다. 대신 BeginWith변수가 필요하다.