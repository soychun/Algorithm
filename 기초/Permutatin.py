# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# DFS를 사용해서 풀이 가능

# 아래 코드는 유튜브 딩코딩 _순열_재귀이용
def dfs(L):
    if len(s)==m:  #dfs의 종료조건이 중요하다  L==m:으로 해도 됨
        print(' '.join(map(str,s)))

    else:
        for i in range(len(n)):
            if v[i]:
                continue
            else:
                v[i]=True
                s.append(n[i])
                dfs(L+1)
                v[i]=False
                s.pop()
n = [1,2,3,4]
m = 3
s = []
v = [False]*len(n)
dfs(0)

# 1 2 3
# 1 2 4
# 1 3 2
# 1 3 4
# 1 4 2
# 1 4 3
# 2 1 3
# 2 1 4
# 2 3 1
# 2 3 4
# 2 4 1
# 2 4 3
# 3 1 2
# 3 1 4
# 3 2 1
# 3 2 4
# 3 4 1
# 3 4 2
# 4 1 2
# 4 1 3
# 4 2 1
# 4 2 3
# 4 3 1
# 4 3 2




# https://velog.io/@yusuk6185/%EB%B0%B1%EC%A4%80-15649-N%EA%B3%BC-M-1-%ED%8C%8C%EC%9D%B4%EC%8D%AC-with-%EB%B0%B1%ED%8A%B8%EB%9E%98%ED%82%B9


# n = 4
# m = 3
#
# s = []
# visited =[0]*(n+1)
# def dfs():
#     if len(s)==m:
#         print(s)
#         return
#     for i in range(1,n+1):
#         if visited[i]==1:
#             continue
#         visited[i] = 1
#         s.append(i)
#         dfs()
#         s.pop()
#         print((s))
#         print(visited)
#         visited[i]=  0

