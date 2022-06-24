'''
회전하는 큐
'''

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
Q = deque()
for i in range(n):
    Q.append(i+1)
    # 1부터 n까지의 수를 Q라는 큐에 삽입
want = map(int, sys.stdin.readline().split())
# 찾고자하는 수를 입력 받음

total = 0
for w in want:
    i = 0
    while w != Q[i]:
        # 입력받은 값과 Q안에 있는 값을 찾을떄까지
        i += 1
        # 1씩더해서 찾고자하는값 인덱스 값 찾기
    i = len(Q) - i if len(Q) - i < i else -i
   # 만약에 찾고자하는 인덱스가 뒤로 돌려야 이득일때는 len(Q) - i
   # 앞으로 돌려야 이득일때는 -i
    Q.rotate(i)
    # 로테이트 모듈로 Q를 i 만큼 돌림
    total += abs(i)
    # abs는 절대값으로 바꿔줌
    Q.popleft()
    # 값을 찾았으니 그 값을 없애줌

print(total)
