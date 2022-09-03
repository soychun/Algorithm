#
# n = int(input())
# for _ in range(n):
#     a,b,c = map(int,input().split())
#     sum = 0
#     for x in range(1,a+1):
#         for y in range(1,b+1):
#             for z in range(1,c+1):
#                 if x%y == y%z:
#                     if y%z == z%x:
#                         sum+=1
#     print(sum)

n = int(input())
s = list(map(int, input().split()))
t_b = 0
s_b = 0
for i in range(n):
    if i ==0:
        t_b = 2
        s_b += t_b
    else:
        if s_b>=100:
            s_b = 0
            t_b = 2
            s_b +=t_b
        else:
            if s[i] == s[i-1]:
                t_b =t_b*2
                s_b +=t_b
                if s_b >= 100:
                    s_b = 100
            else:
                t_b = 2
                s_b +=t_b
                if s_b >= 100:
                    s_b = 100
print(s_b)