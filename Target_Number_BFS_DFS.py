# 코딩테스트 연습
# 깊이/너비 우선 탐색(DFS/BFS)
# 타겟 넘버
# https://programmers.co.kr/learn/courses/30/lessons/43165
### 재귀와 전역변수로 어거지로 품

answer = 0

def bfs(numbers, target, count=0, tmp=0):
    global answer
    if count == len(numbers):
        # print(count, '==', len(numbers))
        if tmp == target:
            # print('\t', tmp, '==', target)
            answer+=1
        return True

    for i in range(2):
        if i:
            bfs(numbers, target, count+1, tmp+numbers[count])
        else:
            bfs(numbers, target, count+1, tmp-numbers[count])


def solution(numbers, target):
    bfs(numbers, target)
    return answer



### 아주 훌륭하고 아름다운 풀이법 ###
'''
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
'''---
