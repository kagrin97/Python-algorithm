def solution(s):
    total_cnt = 0
    zero_cnt = 0

    while True:
        if s != '1': # 1이 될떄까지 반복
            total_cnt += 1
            zero_cnt += s.count('0') # 0의개수 추가
            s = s.replace('0', "") # s에서 0제거
            s = format(len(s), 'zero_cnt') # s의 길이의 2진수 생성
        else:
            return [total_cnt, zero_cnt] # s == '1' 이라면 리턴

s = "1111111"
print(solution(s))

