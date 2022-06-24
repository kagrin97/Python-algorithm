def solution(brown, yellow):
    s = brown + yellow # 총 격자 개수

    for i in range(s, 2, -1): # 2이하인 1은 나눠도 의미가 없기 때문에
        if s % i == 0: # 나눠지면(약수) 세로(a) * 가로(i) = s 가 성립하기 때문에
            a = s // i 
            if yellow == (i-2) * (a-2): # 노란 격자수와 만족한다면 -2를 한이유는
                return [i, a]           # y는 b에 비해 가로세로가 2씩 부족하기 떄문

b = 10
y = 2
print(solution(b, y))
