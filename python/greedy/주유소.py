'''
주유소
'''

import sys

n = int(sys.stdin.readline())  # 도시의 개수
road = []
price = []
road = list(map(int, sys.stdin.readline().split()))  # 도로의 거리 입력
price = list(map(int, sys.stdin.readline().split()))  # 도시마다의 가격

result = 0  # 결과 값
price_min = price[0]  # 첫번쨰 도시의 가격을 미리 저장해야 min이 오류가 안남

for i in range(n-1):  # 마지막 도시는 빼고 반복한다.
    if i == 0:
        result += price[0] * road[0]
# 만약 첫번째 도시일 경우 다음 도시로 가기위한 최소한의 기름을 구입
    else:
        price_min = min(price_min, price[i])
        result += price_min * road[i]
# 첫번쨰 도시가 아닐경우 지금 기름 가격과 현재까지 최저 금액을 비교
# 최저금액 을 다음 도시까지 거리 구입후 다음 도시에서도 마찬가지로 진행
print(result)
