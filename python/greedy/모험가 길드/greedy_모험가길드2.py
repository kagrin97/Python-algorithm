n = int(input())
x = list(map(int, input().split()))
result = 0
group = 0
x.sort()

for i in x:
    result += 1
    if i == result:
        group += 1
        result = 0

print(group)

'''
두번쨰로 풀었을때는 9번쨰 줄을 <= 가 아닌 == 도 썼는데
어차피 오름차순으로 정렬을 했기때문에 == 도 맞는 답이된다.
'''
