s = input()
count0 = 0  # 전부 0으로 바꾸는 횟수
count1 = 0  # 전부 1로 바꾸는 횟수

if s[0] == '1':  # 헤드부분에 값이 1이라면 1을 0으로 바꾸는 카운터 증가
    count0 += 1
else:           # 그반대 증가
    count1 += 1

for i in range(len(s) - 1):  # 전체 길이에서 -1 하면 맨뒤에 있는 숫자부터 반복이 된다
    if s[i] != s[i + 1]:    # 현재 원소와 다음 원소가 다르고
        if s[i + 1] == '1':  # 다음원소가 1이라면 0 카운터 증가
            count0 += 1
        else:                   # 다음 원소가 0일경우 1 카운터증가
            count1 += 1

print(min(count0, count1))  # 두 횟수중 가장 작은 값을 출력
