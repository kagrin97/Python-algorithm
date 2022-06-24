import sys
input = sys.stdin.readline

n, m = map(int, input().split())
train_list = [[0] * 20 for _ in range(n)]
for i in range(m):
    o = list(map(int, input().split()))

    if o[0] == 1:                   # 1번 i번쨰 기차에 x번 좌석에 사람 태움
        i, x = o[1]-1, o[2]-1
        if train_list[i][x] == 0:
            train_list[i][x] = 1

    elif o[0] == 2:                 # 2번 i번쨰 기차에 x번 좌석에 사람 하차
        i, x = o[1] - 1, o[2] - 1
        if train_list[i][x] == 1:
            train_list[i][x] = 0

    elif o[0] == 3:                 # 3번 i번째 기차 뒤로 밀려남
        i = o[1] - 1
        train_list[i] = [0] + train_list[i][:-1]

    elif o[0] == 4:                 # 4번 i번째 기차 앞으로 떙김
        i = o[1] - 1
        train_list[i] = train_list[i][1:]
        train_list[i].append(0)

a = set(list(map(tuple,train_list)))    # 배열들 중복 검사를하는 방법 튜플->리스트->집합
print(len(a))

# 맨처음 3번 명령어를 실행할때 맨앞에 insert로 0을 넣어 줬더니 시간초과가 나와서 배열 합치기를
# 사용을 하였고 + 입력을 sys로 받아서 훨씬 빨라짐 (sys가 진짜 빠름)
