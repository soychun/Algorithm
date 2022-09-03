def factorial(n):
    result = 1
    for i in range(1,n+1):
        result = result*i
    return result

def factorial_recurse(n):
    if n == 0:
        return 1
    else:
        return n*factorial_recurse(n-1)

    # n! = n * (n-1)을 그대로 코드로 구현
print(factorial(10))
print(factorial_recurse(10))