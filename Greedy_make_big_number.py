# 큰 수 만들기
# 탑욕법(Greedy)
# https://programmers.co.kr/learn/courses/30/lessons/42883
#
# 처음엔 combination 써서 쉽게 되는 줄 알았는데 순서가 바뀌면 안됐다.
# [1, 0, 0, 0] 같은 식으로 인덱스를 combination에 넣을까하다가.. 그냥 재귀로 접근했다
# 경우는 다 되는 것 같은데, 런타임 에러가 뜬다.. 시간이 오래 걸리는 방법인가보다.

# import itertools

# def solution(number, k):
#     return max(list(map(int, map(''.join, itertools.permutations(number, len(number)-k)))))


answer = 0

def solution(number, k):
    global answer

    if k==0:
        answer = max(int(number), answer)
        return 0

    for i in range(len(number)):
        solution(number[:i]+number[i+1:], k-1)

    return str(answer)
