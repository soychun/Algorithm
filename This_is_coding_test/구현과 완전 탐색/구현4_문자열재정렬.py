s_ = sorted(list(input()))
c = 0
i =0
for s in s_:
    if ord(s)<ord('A'):
        c+= int(s)
        i+=1
print(''.join(s_[i:])+str(c))

# 풀이 방법에는, 새로운 리스트에 문자를 저장하는 방법이 있다.


# 나동빈 풀이
data = input()
result = []
value=0
for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)
result.sort()
if value !=0:
    result.append(str(value))
print(''.join(result))