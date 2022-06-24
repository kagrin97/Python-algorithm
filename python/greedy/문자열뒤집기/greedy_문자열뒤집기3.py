s = input()
count0 = 0
count1 = 0

if s[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(1, len(s)):  # 두번째 값부터 마지막까지 비교
    if s[i] != s[i - 1]:  # 두번째 값부터 비교하기때문에 첫번 자리 부터 비교
        if s[i] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))
