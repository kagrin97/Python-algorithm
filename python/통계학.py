'''
파이썬 통계학
'''
from collections import Counter  # 빈도값을 위한 함수
import statistics  # 중앙값을 구하기위한 함수
import sys  # 연산속도 up

n = int(sys.stdin.readline())
num = []

for i in range(n):
    num.append(int(sys.stdin.readline()))


def mode(x):
    modes = Counter(x).most_common()
    # 배열안에 dic 형식으로 최빈값부터 2번째로 자주 나오는 수를 반환함
    if len(x) > 1:
        # 안에 값이 한가지면 그값만 반환
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]
            # 최빈값이 가장큰 값과 그 다음 값이 같으면 다음값이 2번째이기때문에 그값 반환
        else:
            mod = modes[0][0]
            # 아닐경우 가장 큰값을 반환
    else:
        mod = modes[0][0]
        # 최빈값이 하나만 존재할경우

    return mod


result_1 = sum(num) / n
print('%.f' % result_1)  # 산술평균, 1에자리에서 올려야함
print(statistics.median(num))  # num안에 중앙값을 구해줌
num.sort()  # 최빈값이 여러개 일수있으므로 작은값부터 정렬
print(mode(num))  # 최빈값 함수 호출
print(max(num) - min(num))  # 제일큰값과 제일 작은값의 차이
