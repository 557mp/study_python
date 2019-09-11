## 스택/큐
## 기능개발
## https://programmers.co.kr/learn/courses/30/lessons/42586#


def solution(progresses, speeds):
    ## 0 ~ i in p      if -1
    answer = []
    stored = 0
    tmp = 0

    while(sum(answer)<len(progresses)):
        for i in range(len(progresses), 0, -1):
            if sum(progresses[:i]) == -(i):
                # print('if 1')
                tmp = i-stored
                stored = i

                if tmp>0:
                    # print('if 2')
                    answer.append(tmp)
                break

        for i, sp in enumerate(speeds):
            if sp == 0:
                pass
            elif progresses[i] >= 100:
                progresses[i] = -1
                speeds[i] = 0
            else:
                progresses[i] += sp

        # print(progresses, answer, '\n')

    return answer
