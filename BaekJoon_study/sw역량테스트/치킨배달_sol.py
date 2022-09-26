from collections import deque

n,m = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))

def loc(g):
    loc_list = []
    hom_list = []
    for r in range(n):
        for c in range(n):
            if g[r][c]==2:
                loc_list.append([r,c])
            elif g[r][c]==1:
                hom_list.append([r,c])
    return loc_list,hom_list

loc_list,hom_list = loc(g)   # 위치 추출


def distance(r1,c1,r2,c2):
    return abs(r1-r2)+abs(c1-c2)
def chicken_distance(hom_list,loc_list):
    total_d = 0
    for D_h in hom_list:
        min_d = 100
        for D_c in loc_list:
            min_d = min(min_d,distance(D_h[0],D_h[1],D_c[0],D_c[1]))
        total_d+=min_d
    return total_d

min_ch_d = 10000000  #최소값 잡을 때는 엄청나게 큰 숫자로 잡아두자
s = []
def dfs(s,L):
    global min_ch_d
    if len(s)==m:
        # print(s)
        # print(chicken_distance(hom_list,s))
        min_ch_d = min(min_ch_d,chicken_distance(hom_list,s))
        return
    elif L==len(loc_list):
        return
    s.append(loc_list[L])
    dfs(s,L+1)
    s.pop()
    dfs(s,L+1)
dfs(s,0)
print(str(min_ch_d))
