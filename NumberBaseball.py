# 완전탐색 > 숫자 야구
# https://programmers.co.kr/learn/courses/30/lessons/42841
# 하드 코딩으로 해봤는데, 일단 여기까지만..


def solution(baseball):
    # 경우의 수를 나눠봐야 하나?
    # 너무 많다.

    # 111 ~ 999 모두 해보자. = tmp
    # 확인은 어떻게 하지?
    # for bb in baseball:
    # 스트라이크 확인
    # for i in range(3):
    #  tmp[i] == ? -> strike ++;
    # 볼 확인
    # for i in range(3):
    #  bb.count(tmp[i]) -> ball_tmp ++;
    # candi 만들어지면 그걸가지고 다음 탐색 //// 아닌 경우 제외

    # 예) 1개의 자료만 있을 경우?
    # A: 123, 1, 1
    # --> bb = [123, 1, 1]
    # for candi in range(111, 999, 1):
    # 111일때만 따지면?
    # for i in range(3):
    #  if candi[i] == str(bb[0])[i]:
    #   strike += 1
    # if strike != bb[1]:
    #  candidate.remove(candi)
    #
    # for i in range(3):
    #  ball_count = bb[0].count(candi[i])
    # if ball_count != b[2]:
    #  candidate.remove(candi)

    candidate = [ str(i) for i in range(111,1000,1)]
    # print(candidate)

    for candi in candidate:
        # print(type(candi))
        # print(candi[0])
        strike = 0
        ball_count = 0

        for bb in baseball:
            bb[0] = str(bb[0])
            for i in range(3):
                if candi[i] == bb[0][i]:
                    strike += 1
            try:
                if strike != bb[1]:
                    candidate.remove(candi)
            except:
                pass

            for i in range(3):
                ball_count = bb[0].count(candi[i])
            try:
                if ball_count != bb[2]:
                    candidate.remove(candi)
            except:
                pass

    return len(candidate)
