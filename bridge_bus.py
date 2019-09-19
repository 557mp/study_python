# 다리를 지나는 트럭
# https://programmers.co.kr/learn/courses/30/lessons/42583
# 5번 케이스 시간 초과 난다.
# 다른 풀이법을 보니, 약 2배 정도 더 오래 거리는 것 같다.
# 속상하다.
# 다른 풀이를 봤으니, 다음에 다시 풀어봐야겠다.

def solution(br_len, br_w, tr_w):
    time = 0
    br_arr = [0]*br_len
    sum_end = 0
    end_flag = sum(tr_w)
    tr_tmp=0

    while(1):
        if sum_end>=end_flag:
            return time-1

        if sum(br_arr[1:])+tr_tmp <= br_w:
            br_arr.append(tr_tmp)
            tr_tmp = 0 if not tr_w else tr_w.pop(0)
        else:
            br_arr.append(0)

        # shifting
        sum_end+=br_arr.pop(0)
        time += 1

    return False
