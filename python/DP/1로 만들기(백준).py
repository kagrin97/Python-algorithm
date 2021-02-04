import sys

x = int(sys.stdin.readline())

d = [0] * (10**6+1)

for i in range(2, x+1):
    d[i] = d[i - 1] + 1
    # 1을 뺴는 경우 
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
        # 2로도 나눠지고 1로뺀 수랑 비교 후 갱신
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)


print(d[x])

'''
위 문제는 이코테와 다르게 x의 값이 최대 10의6승이고
x가 5로 나눈 경우는 없다
3번쨰 줄을 이렇게 구할 수도 있다
d = [0 for _ in range(x + 1)]
'''

