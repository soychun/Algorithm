n = 4
n_list = [i+1 for i in range(n)]
r = 3
print(n_list)
v = [0]*n
s = []
# def dfs(L):  #포문돌면서 넣고 표시 재귀 빼기
#     if L==r:
#         print(s)
#     else:
#         for d in range(n):
#             if v[d]==0:
#                 v[d]=1
#                 s.append(n_list[d])
#                 dfs(L+1)
#                 v[d] = 0
#                 s.pop()
# dfs(0)

s = []
def dfs_combi(L,B):
    if L==r:
        print(s)
    else:
        for i in range(B,n):
            s.append(n_list[i])
            dfs_combi(L+1,i+1)
            s.pop()
dfs_combi(0,0)