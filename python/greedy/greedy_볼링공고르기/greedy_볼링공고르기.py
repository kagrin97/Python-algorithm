n, m = map(int, input().split)
data = list(map(int, input().split()))
array = [0] * 11  # 1부터 10까지 무게를 담는 리스트
result = 0

for i in data:
    array[i] += 1 # 각무게마다의 개수 카운트

for i in range(1, m + 1): # 1무게부터 최대무게까지 반복
    n -= array[i] # a가 고른 볼링공말고 다른공 저장 같은숫자 연속x
    result += array[i] * n # a와b가 같은수가 안되면서 최대로 고르는 경우의수

print(result)