'''
링 : 분수를 이용한 문제
'''


from fractions import Fraction
# 분수를 계산해주는 모듈
N = int(input())
# 링의 개수
ring_list = list(map(int, input().split()))
# 링의 둘레
for i in range(1, N):
    answer = Fraction(ring_list[0], 1)/Fraction(ring_list[i], 1)
    # 제일앞 링둘레와 그뒤에있는 링의 둘레를 나눈값을 넣어준다
    print(answer.numerator, '/', answer.denominator, sep='')
    #numerator <- 분모, denominator <- 분자
