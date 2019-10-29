# 2018 카카오 온라인 채용 코딩 문제
# [1차]비밀지도

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        tmp = ''
        t1 = format(arr1[i],'b').zfill(n)
        t2 = bin(arr2[i])[2:].zfill(n)
        for j in range(n):
            if t1[j] == '1' or t2[j] == '1':
                tmp += '#'
            else:
                tmp += ' '
        answer.append(tmp)
    return answer
