# 곱하기 혹은 더하기
S = input()
result = 0
for s in S:
    # print(s)
    s = int(s)
    if(s==0 or s==1 or result==0 or result==1):
        result = result + s
        # print('if')
    else:
        result = result * s
        # print('else')
print(result)
