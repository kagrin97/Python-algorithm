'''
최대 힙
'''

import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, (-num))
    else:
        try:
            print(-1 * heapq.heappop(heap))
        except:
            print(0)

'''
처음 문제를 풀었을때는 스택으로 append를 써서 max값을 이용하는 방법을
사용하였을떄는 시간 초과가 발생하였다.
heap을 이용하면 최대값 최소값을 이용한 문제를 만났을때 훨씬 빠른 속도를 낼
수가 있다.
heapq은 min만 제공하기 떄문에 max를 위해서는 14줄에 수를 넣을때
-를 한 상태로 넣으면 가장 작은수부터 차례대로 쌓인다.
17줄에 가장 작은수를 꺼내고 거기에 -1을 곱해 양수로 바꿔준다
'''