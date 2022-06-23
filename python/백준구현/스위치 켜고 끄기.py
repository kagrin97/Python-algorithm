sw_n = int(input())
switch = list(map(int, input().split()))
st_n = int(input())

for _ in range(st_n):
    sex, num = map(int, input().split()) # 1남, 2여
    tmp = []

    if sex == 1:                            # 남성일 경우
        for i in range(1, len(switch)+1):
            if i % num == 0:                # 해당 스위치 배수를 뒤집어줌
                if switch[i-1] == 1:
                    switch[i - 1] = 0
                else:
                    switch[i - 1] = 1
    else:                                   # 여성일 경우
        tmp.append(num-1)                   # 기준 스위치 위치를 넣어줌
        if num != 1:                        # 기준 스위치가 맨앞이 아닐때
            min_val = min(num-1, len(switch)-num)  # 양옆의 최소 스위치 길이를 알아냄
            for i in range(1, min_val+1):
                if switch[num-1-i] != switch[num-1+i]:  # 양옆 스위치 상태가 다르면 종료
                    break
                tmp.append(num-1-i)                 # 왼쪽 스위치 위치
                tmp.append(num-1+i)                 # 오른쪽 스위치 위치

    if tmp:                              # 여성이 실행했으면
        for i in tmp:                   # 바꿀 위치를 꺼내서 바꿔줌
            if switch[i] == 1:
                switch[i] = 0
            else:
                switch[i] = 1
ans = []
tmp = []
for i in switch:
    if len(tmp) == 20:          # 문제에서 20개씩 출력하라해서 20개씩 리스트를 만들어줌
        ans.append(tmp)
        tmp = []
        tmp.append(i)
    else:
        tmp.append(i)
ans.append(tmp)

for i in ans:           # 출력
    print(*i)