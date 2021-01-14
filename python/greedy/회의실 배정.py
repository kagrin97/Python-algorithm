import sys

n = int(sys.stdin.readline())

conference = []
# 회의 리스트
cnt = 0
last = 0
# 끝나는 시간

for i in range(n):
    start, end = map(int, sys.stdin.readline().split())
    conference.append((start, end))
    # 시작 시간과 끝나는 시간을 각각 넣어준다

conference = sorted(conference, key=lambda a: a[0])
conference = sorted(conference, key=lambda a: a[1])
# sorted를 이용해 시작시간 순을 정렬후 다시 종료 시간후로 정렬
# sort로 했을때는 틀렸다고나오고 a[0], a[1]로 합치면 밑에 last가 오류난다

for i, j in conference:
    if i >= last:
        cnt += 1
        last = j
# 시작시간과 끝난 시간을비교해 같거나 크면 회의를 시작해서 카운트 올리고 끝나는 시간을
# 방금전 끝난 시간으로 초기화

print(cnt)
