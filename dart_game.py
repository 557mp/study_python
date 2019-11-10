# 2018 KAKAO BLIND RECRUITMENT
# [1차] 다트 게임
# https://programmers.co.kr/learn/courses/30/lessons/17682
# 하드코딩..

def SDT(string):
    num = string[0]
    if string[1] == '0':
        num = '10'
        sdt = string[2]
    else:
        sdt = string[1]

    if sdt == 'S':
        return int(num)
    elif sdt == 'D':
        return int(num)**2
    elif sdt == 'T':
        return int(num)**3
    else:
        print('(error) no S, D, T')
        return None

def solution(data):
    d_arr = []
    i_arr = []
    n_arr = []
    for i, d in enumerate(data):
        if i == 0:
            pass
        elif d=='0' and data[i-1] =='1':
            pass
        elif d<='9' and d>='0':
            i_arr.append(i)

    d_arr.append(data[:i_arr[0]])
    d_arr.append(data[i_arr[0]:i_arr[-1]])
    d_arr.append(data[i_arr[-1]:])
    # print(i_arr, d_arr)

    for i in range(len(d_arr)):
        n_arr.append(SDT(d_arr[i]))
    # print(n_arr)

    for i, d in enumerate(d_arr):
        if d[-1] == '#':
            n_arr[i] = n_arr[i] * (-1)
        elif i==0 and d[-1] == '*':
            n_arr[0] = n_arr[0] * 2
        elif i>0 and d[-1] == '*':
            n_arr[i-1] = n_arr[i-1] * 2
            n_arr[i] = n_arr[i] * 2

    # print(n_arr)
    return(sum(n_arr))



    # 다른 사람의 풀이를 보니, 정규 표현식을 활용하였더라.
    # 나도 정규식을 자유롭게 사용할 수 있도록 연습해야겠다.
    # 정규식을 이용한 해답은 다음과 같다.
    # 출처: 프로그래머스
    # https://programmers.co.kr/learn/courses/30/lessons/17682/solution_groups?language=python3

    import re


def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer
