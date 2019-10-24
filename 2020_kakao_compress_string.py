# [2020카카오공채] 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057
# 정확성: 28.0
# 합계: 28.0 / 100.0
# 거의 하드코딩이라고 생각했는데 정확성이 엉망이다.



def solution(s):
    max_num = len(s)//2
    answer = len(s)

    for unit in range(1, max_num+1, 1):
        # unit = 2 # 2개 단위일 때,
        tmp_ans = len(s)
        flag = False
        tmp = 'START'
        for i in range(len(s)):
            # print('\n', tmp, '\t', s[unit*i:unit*(i+1)])
            if tmp=='':
                if flag:
                    tmp_ans += 1
                break
            elif tmp == s[unit*i:unit*(i+1)]:
                if flag:
                    tmp_ans += 1
                # print('boom! flag: ', flag)
                tmp_ans -= unit
                flag = True
            else:
                # print('nah~ flag: ', flag)
                if flag:
                    tmp_ans += 1
                    flag = False
                else:
                    pass

                tmp = s[unit*i:unit*(i+1)]
        answer = min(answer, tmp_ans)
        # print('------------------', tmp_ans, '\n\n')
    return answer
