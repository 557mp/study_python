###### 프로그래머스 - 해쉬 - 베스트앨범
###### 런타임 초과 ㅠㅠ

def solution(genres, plays):
    num_len = len(plays)
    ## plays --> index 와 같다 ##
    
    ## 장르별로 모으기 ##
    ## 2차 행렬로 만들어 놓기 ##
    g_list = list(set(genres))
    print('* genres: ', g_list)
    # row_g = [ [0]*num_len ] * len(g_list)   <-- 문제 발생 하더라.. ?!
    row_g = [ [ 0 for _ in range(num_len) ]   for _ in range(len(g_list)) ]

    for i in range(num_len):
        for g in range(len(g_list)):
            if genres[i] == g_list[g]:
                row_g[g][i] = plays[i]
    print('* row(genre) + col(plays) \n\t--> ', row_g)

    gen_sum = [ sum(row_g[i]) for i in range(len(g_list))]

    gen_sum_list = {}
    for g in range(len(g_list)):
        gen_sum_list[gen_sum[g]] = g_list[g]
    print('* sum dictionary: ', gen_sum_list)

    gen_sum_list = sorted(gen_sum_list.items(), reverse=True)
    print('* sum dictionary(sorted, list): ', gen_sum_list)

    sorted_g_list=[]
    for a, b in gen_sum_list:
        sorted_g_list.append(b)
    print('* (new)sorted genre list: ', sorted_g_list)


    print('\n')
    ## Each 장르, 안에서 비교하기 ##
    ## sort , [0] [1] 값 찾아 나서기 -> 찾는 것은 원래 plays 에서 ##
    answer = []

    for mem in sorted_g_list:
        tmp_num = g_list.index(mem)
        print(tmp_num)
        print(row_g[tmp_num])

        tmp_1 = plays.index(sorted(row_g[tmp_num], reverse=True)[0])
        tmp_2 = plays.index(sorted(row_g[tmp_num], reverse=True)[1])
        print('#1 = ', tmp_1 , '\t #2 = ', tmp_2)

        answer.append(tmp_1)
        answer.append(tmp_2)

    return answer
