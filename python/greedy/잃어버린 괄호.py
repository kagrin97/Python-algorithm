'''
잃어버린 괄호
'''

arr = input().split('-')
# -를 기준으로 식을 받는다 22-23+34 -> 22, 23+34
sum = 0

for i in arr[0].split('+'):
    sum += int(i)
# 0번째 값이 + 가있으면 해체하고 아닌경우에도 sum에 더한다
for i in arr[1:]:
    for j in i.split('+'):
        sum -= int(j)
# 1번쨰 값부터 끝까지 비교해서 +가있으면 그값을 다 더한후 뺴주고
#  수가 하나인경우에도 그값을 빼준다
print(sum)
