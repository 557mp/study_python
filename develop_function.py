### 프로그래머스 - 스택/큐 - 기능개발
# https://programmers.co.kr/learn/courses/30/lessons/42586

#######
# 두 가지 방법을 사용.
# 1. 하드코딩(밑)
# 2. 덜 하드코딩(위))
#
# 1번은 1개 빼고 모두 런타임 에러
# 2번은 즉당히 3개 빼고 런타임 에러..
#######

def solution(p, s):
    answer = []
    tmp = 0
    order = 0

    while(order<len(p)):

        for i in range(len(p)):
            p[i] += s[i]

        # print(p)
        if p[order] == -1:
            order +=1

        elif p[order] >= 100:
            order += 1

            ### 100이 넘는 갯수 세기
            ans = 0
            for i in range(len(p)):
                if p[i] >= 100:
                    ans += 1

                    ### 100이 넘는 것들 0으로 바꾸기, 앞으로 세지 않는다.
                    p[i] = -1
                    s[i] = 0

            answer.append(ans)

    return answer


#         if p[order]>=100:
#             answer.append(ans-tmp)
#             tmp = ans
#             ans = 0

    return answer

# def solution(progresses, speeds):
#     answer = []

#     while(len(progresses)>0):
#         tmp_arr=[]

#         if progresses[0] >= 100:
#             for i in range(len(progresses)):
#                 if progresses[i] >= 100:
#                     tmp_arr.append(i)

#         else:
#             for i in range(len(speeds)):
#                 progresses[i] += speeds[i]

#         if len(tmp_arr)>0:
#             answer.append(len(tmp_arr))

#         for t in tmp_arr:
#             progresses.pop(t)
#             speeds.pop(t)

#     return answer

#     ## while 없어질 때

#     ## 시간 흐름, t

#     ## tmp = 1
#     ## 완성되는 것 있으면 && 맨 앞에 것 외에 완성되면 tmp++;
#     ## 맨 앞에 것이 완성되면, answer.append(tmp)
