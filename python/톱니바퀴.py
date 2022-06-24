import sys
input = sys.stdin.readline
from collections import deque

def check_right(start, dirs):
    if start > 4 or gears[start-1][2] == gears[start][6]:
        return # 현재 톱니가 4라서 오른쪽을 체크할수 없거나 
                # 바로 오른쪽 톱니가 회전가능하면 탈출
    if gears[start-1][2] != gears[start][6]: # 바로 오른쪽 톱니가 회전이 안되면
        check_right(start+1, -dirs) # 더 오른쪽에 있는 톱니들 조사 -를해줘야 짝수번째 마다 같은 회전을 같게됨
        gears[start].rotate(dirs) # 오른쪽 톱니 회전

def check_left(start, dirs):
    if start < 1 or gears[start][2] == gears[start+1][6]:
        return 

    if gears[start+1][6] != gears[start][2]:
        check_left(start-1, -dirs)
        gears[start].rotate(dirs)

gears = {}
for i in range(1, 5):
    gears[i] = deque(map(int, input().strip())) # 각톱니의 info를 딕셔너리, 큐 형태로 저장
n = int(input())

for _ in range(n):
    num, dirs = map(int, input().split())

    check_right(num+1, -dirs) # 왼쪽을 체크
    check_left(num-1, -dirs) # 오른쪽 체크

    gears[num].rotate(dirs) # 기준 톱니바퀴 회전
result = 0
for i in range(4):
    result += (2**i) * gears[i+1][0] # 각점수마다 저장
print(result)

'''
이 문제는 평소 알지 못했던 rotate 함수를 알수가 있었다 rotate(1)은 오른쪽으로 회전하고
rotate(-1)은 반대로 회전한다 