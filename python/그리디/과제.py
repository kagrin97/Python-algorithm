N = int(input())
homework = []
for _ in range(N):
    d, w = map(int, input().split())
    homework.append((d, w))

homework.sort()
can = []
date = homework[-1][0] # 마감일이 제일 많이남은 마감날
answer = 0
while True:
    if date == 0: # 마감일이 0이라면 종료
        break
    while homework and homework[-1][0] >= date: # 남은 과제가 있고 수행가능한 과제일경우
        can.append(homework.pop()[1]) # 과제의 값 추가
    date -= 1 # 다음날
    if not can: 
        continue
    can.sort() # 오름차순정렬
    answer += can.pop() # 가장큰값 추가
print(answer)

'''
이문제의 최대해를 찾는 아이디어는 첫날부터 세는 것이아닌 마감일부터 세는것
으로 먼저 마감일이 많이 남은 순 -> 점수가 높은 순으로 정렬한후에
6일쨰부터 1일쨰까지 반복문을 돌아서 가장큰 값을 가진 과제를 수행한다
'''