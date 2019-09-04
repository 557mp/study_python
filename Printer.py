### programmers - stack/queue - Printer
# https://programmers.co.kr/learn/courses/30/lessons/42587


def solution(priorities, location):
    #### 하드코딩 ####
    answer = 1

    ##### while #####
    while(len(priorities)>0):
        # if 종결문 , return answer
        # 즉, location =0 일 때
        if location == 0 and priorities[0] == max(priorities):
            return answer

        elif location != 0 and priorities[0] == max(priorities):
            priorities.pop(0)
            answer += 1
            location -= 1

        elif location == 0:
            priorities.append(priorities.pop(0))
            location = len(priorities)-1

        else:
            priorities.append(priorities.pop(0))
            location -= 1




    ## 아니다. rotate

    ## 다시.... 0번째, 가장 높나?

    ## 가장 높다, pop(0) , while 나가기

    #### 문제는, pop, roate 할 때, index 변화가 같이 이루어져야 한다.
    #### index 0 일때 --> pop : return 값,   rotate : 함께 rotate
