# 첫번째 쓴 코드
import sys
input = int(sys.stdin.readline())
def self_f(input):

    if input == 0:
        result = 1
    else:
        result = input * self_f(input - 1)

    return result

print(self_f(input))


# 수정한 코드
import sys
n = int(sys.stdin.readline())
def p(n):
    if n == 0:
        return 1
    else:
        return n*p(n-1)
print(p(n))