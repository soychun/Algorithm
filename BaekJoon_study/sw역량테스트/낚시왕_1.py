

r,c,m = map(int,input().split())
s_size = [[0]*c for _ in range(r)]
s_speed = [[0]*c for _ in range(r)]
s_d = [[0]*c for _ in range(r)]
for _ in range(m):
    s_r,s_c,s,d,z = map(int,input().split())
    s_size[s_r-1][s_c-1] = z
    s_speed[s_r-1][s_c-1] = s
    s_d[s_r-1][s_c-1] = d

total_s_size = 0
dx = [(-1,1),(1,-1),(0,0),(0,0)] # 위,아래, 오른쪽, 왼쪽
dy = [(0,0),(0,0),(1,-1),(-1,1)]
print(r,c,m)
print(s_size)

for i in range(c):
    sorted(s_size)
    tmp_s = 0
    for tmp in range(r):
        if s_size[tmp][i]>0:
            tmp_s = tmp
            break
    s_size[tmp_s][i],s_speed[tmp_s][i],s_d[tmp_s][i] = 0,0,0
    for r_ in range(r):
        for c_ in range(c):
            if s_size[r_][c_]>0:
                r_tmp = r_
                c_tmp = c_
                d = 0
                s_speed_tmp = s_speed[r_][c_]
                while True:
                    nr_tmp = r_tmp + dx[s_d[r_][c_]][d]
                    nc_tmp = c_tmp + dy[s_d[r_][c_]][d]
                    if nr_tmp>=r or nc_tmp>=c or nr_tmp<0 or nc_tmp<0:
                        d +=1
                        continue
                    if s_speed_tmp==0:
                        break
                    s_speed_tmp = s_speed_tmp-1
                    r_tmp = nr_tmp
                    c_tmp = nc_tmp

                s_size[r_tmp][c_tmp] = s_size[r_][c_]
                s_size[r_tmp][c_tmp] = s_size[r_][c_]
