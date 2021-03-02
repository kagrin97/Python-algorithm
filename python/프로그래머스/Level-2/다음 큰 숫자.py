def solution(n):

    num_2 = str(format(n, 'b')) # 2진수변환후 count사용을 위한 str뱐횐
    n_cnt = num_2.count("1") 
    next_num = n 

    while True:
        next_num += 1
        next_num_2 = str(format(next_num, 'b'))
        n2_cnt = next_num_2.count("1")
        if n2_cnt == n_cnt: # 둘다 2진수 변환후 1의 수가 같다면
            return next_num # 다음 값 출력

s = 78
print(solution(s))

'''

