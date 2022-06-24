'''
절대 값 힙
'''

import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap,(abs(num),num))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)

'''
num가 0이 아닐경우 heap에 튜플형식으로 절대값, 실제값을 넣어준다. 14줄
예 : [(3, -3)]
num이 0일 경우 튜플안에 인덱스 1번 값을 제거한다 즉 실제값을 제거후 프린트
값이 없을 경우 0을 출력
'''

