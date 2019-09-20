# 완전탐색 > 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/42839#
# 테스트 케이스는 괜찮은데, 왜 안되는 거지..

from math import sqrt
from itertools import permutations

def solution(numbers):
    answer = 0

    # combinations
    c_arr = list(set(map(int, [''.join(j) for i in range(len(numbers)) for j in permutations(numbers, i+1)])))
    print(c_arr)

    for c in c_arr:
        if c > 1:
            # -----finding prime number------
            sq_c = int(sqrt(c))
            # print(c, sq_c, '<- new')
            for i in range(2, sq_c+2, 1):
                # print(c, i)
                if c%i == 0:
                    break
                if i==sq_c+1:
                    answer += 1
                    # print('!!', c)


    return answer
