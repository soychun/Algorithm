
https://shoark7.github.io/programming/algorithm/3-ways-to-get-binomial-coefficients
[조합론] 이항계수 알고리즘 3가지
동적 계획법 : 기억하며 풀기 (dynamic programing)
    어떤 부분문제를 해결하기 위해 (사용한 값을 재활용) memorization을 활용하여 값을 저장한다
    중복된 부분문제를 한 번만 계산하도록 메모라이제이션을 적용
    복잡한 문제를 서로 중복되지 않는 작은 문제들로 나누어 해결한 후 이를 종합하는 방식
        피보나치 수열로 설명한 블로그 : https://blog.naver.com/chad0909/222670702780

            def fibo(n):
                arr = [0 for i in range(n+1)]
                arr[0] = 0
                arr[1] = 1

                for i in range(2, n+1):
                    arr[i] = arr[i-1] + arr[i-2]
                print(arr)
                return arr[n]
            print(fibo(10))

        추천문제 : https://www.acmicpc.net/problem/11726 2xn타일링
                    https://www.acmicpc.net/problem/9461 파도반 수열


전체 집합에서 아무것도 고르지 않는 방법은 1가지이고, 동시에 모두를 선택하는 것도 한가지 방법뿐이다
이항계수는 두 개의 부분식으로 쪼갤 수 있고, 점점 잘게 쪼갤 수도 있다

이항계수 재귀로 풀기
def bino_coef(n,k):
    if k == 0 or n==k:
        return 1
    return bino_coef(n-1,k) + bino_coef(n-1,k-1)
print(bino_coef(3,2))

하지만 이렇게 하게 되면 부분문제의 중복(overlapping subproblems)으로 함수의 성능이 나쁘다
def print_g(g):
    for i in range(len(g)):
        print(g[i])
def bino_coef(n,r):
    # 1 캐쉬 생성
    cache = [[0 for _ in range(r+1)] for _ in range(n+1)]
    # 캐쉬 초기화, r이 0이거나 n과 r이 같은 경우는 1
    for i in range(n+1):
        cache[i][0] = 1
    for i in range(r+1):
        cache[i][i] = 1
    # 실제로 값을 구함 다 구해서 채워넣고 (n부터 r까지
    for i in range(1,n+1):
        for j in range(1,r+1):
            cache[i][j] =  cache[i-1][j] + cache[i-1][j-1]

    print_g(cache)
    return cache[n][r]

print(bino_coef(6,4))
# ex 3,2
# [1, 0, 0]
# [1, 1, 0]
# [1, 2, 1]
# [1, 3, 3]
# 3

# ex 6,4
# [1, 0, 0, 0, 0]
# [1, 1, 0, 0, 0]
# [1, 2, 1, 0, 0]
# [1, 3, 3, 1, 0]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5]
# [1, 6, 15, 20, 15]
# 15
