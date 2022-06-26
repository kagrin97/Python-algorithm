import sys
input = sys.stdin.readline

N = int(input())
board = list(input().strip())   # E 오른쪽, W 왼쪽
cnt = 0
for i in range(1, len(board)):
    if board[i] == 'W' and board[i-1] == 'E':
        cnt += 1

print(cnt)

# 이 문제는 EW 가 연속되있는 곳은 무한루프가 발생하기 때문에 그곳에 구사과는 무한루프에 빠져서
# 그곳에 무조건 머물기 때문에 EW가 연속된곳의 숫자가 답이다