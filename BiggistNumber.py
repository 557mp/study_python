# 정렬 > 가장 큰 수
# https://programmers.co.kr/learn/courses/30/lessons/42746
# 시간이 너무 길게 나온다.. ㅠㅠ 나름 괜찮은 방법이라 생각했는데 접근 방식이 완전히 틀린 것 같다.

def solution(numbers):
    ns = list(numbers)
    answer = ''

    for i in range(len(ns)):
        tail = ns[i]%10
        while(ns[i]<1000):
            ns[i] = ns[i]*10+tail

    for j in [ i[0] for i in sorted(enumerate(ns), key = lambda x:x[1], reverse = True)]:
        answer+=str(numbers[j])

    return answer



def solution(numbers):
    ns = list(numbers)
    answer = ''

    for i in range(len(ns)):
        if ns[i] == 1000:
            ns[i] = '1000'
        else:
            tail = str(ns[i]%10)
            ns[i] = str(ns[i])
            ns[i] += (3-len(ns[i]))*tail

    for j in [ i[0] for i in sorted(enumerate(ns), key = lambda x:x[1], reverse = True)]:
        answer+=str(numbers[j])

    return answer
