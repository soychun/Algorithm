#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'solution' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. INTEGER x
#

def solution(cost, x):
    import numpy as np

    # Write your code here
    # print(cost)
    # print(x)
    n = len(cost)
    tmp = [i for i in range(n)]  # 숫자
    # print(tmp)
    tmp_g = []  # 경우의 수 담기

    def dfs(L, B, r):  # 지정해주는거부터 돌면서 넣고 빼고
        if L == r:
            # print(s)
            tmp_g.append(list(s))
        else:
            for i in range(B, n):
                s.append(tmp[i])
                dfs(L + 1, i + 1, r)
                s.pop()

    n = len(cost)
    for r in range(1, len(cost) + 1):
        # i개 뽑기 조합
        # print(r,'개 뽑겠스빈다')
        s = []
        dfs(0, 0, r)
    # print('최종입니다')
    # print(tmp_g)
    # print('계산')
    tmp_value = []
    for paint in tmp_g:
        # print(paint)
        value = 0
        for num in paint:
            value += cost[num]
        tmp_value.append(value)
    # print(tmp_value)

    position = list(np.where(np.array(tmp_value) <= x)[0])
    # print(list(position[0]))
    tmp_total = []
    for p in position:
        # print(tmp_g[p])
        sum = 0
        for c in tmp_g[p]:
            sum += 2 ** c
        tmp_total.append(sum)
    # print('tmp_total',tmp_total)
    # print(max(tmp_total)%(10**9+7))
    return max(tmp_total) % (10 ** 9 + 7)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    cost_count = int(input().strip())

    cost = []

    for _ in range(cost_count):
        cost_item = int(input().strip())
        cost.append(cost_item)

    x = int(input().strip())

    result = solution(cost, x)

    fptr.write(str(result) + '\n')

    fptr.close()


def solution(cost, x):
    import sys
    sys.setrecursionlimit(10 ** 6)
    import numpy as np
    n = len(cost)
    pv = [2 ** i for i in range(n)]
    print(cost)
    print(pv)
    res = -1

    def DFS(a, s, time):
        nonlocal res
        if time > x:
            return
        if a == n:
            if s > res:
                res = s
        else:  # 두가지 경우로 나뉜다. 문제를 푸는 경우와 풀지 않는 경우
            DFS(a + 1, s + pv[a], time + cost[a])
            DFS(a + 1, s, time)

    DFS(0, 0, 0)
    print(res)
    return res