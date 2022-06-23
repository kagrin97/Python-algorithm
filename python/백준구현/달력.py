n = int(input())
calender = [0] * 366
ans = 0
for i in range(n):
    start, end = map(int, input().split())
    for a in range(start-1, end):
        calender[a] += 1            # 해당 날짜에 일정을 추가해줌

tmp = []
paper = 0
for i in calender:
    if i == 0 and tmp:      # 일정이 끊어지는 지점
        paper += len(tmp) * max(tmp)    # 가로와 세로를 곱해줌
        tmp = []
    elif i != 0:        # 일정을 넣어줌
        tmp.append(i)
paper += len(tmp)       # 마지막에 남는 일정도 넣어줌
print(paper)

# 이문제는 처음에 캘린더를 [0] * 365로 했더니 틀렸다고 나왔다
# 366으로 바꾸고 맞았는데 아직도 잘이유를 모르겠네