n = int(input())

lines = []

for _ in range(n):
    a, b = map(int, input().split())
    lines.append((a, b))
    # 리스트 안에 리스트 형태로 저장
lines.sort()

lines_b = list(map(lambda x: x[1], lines))
# 두번쨰 인덱스를 list 형태로 따로 빼기
result = [1] * n
# LIS 실현
for i in range(n):
    for j in range(i):
        if lines_b[i] > lines_b[j]:
            result[i] = max(result[i], result[j] + 1)

print(n - max(result))

'''
전깃줄 문제는 전체 값 - 무조건 연결되는 수 = 빼야할 전깃줄
를 바탕으로 만들었다. 기본적으로 a줄이 오름차순이고 b줄도 오름차순
이면 모든 줄이 연결되기 때문에 제거 해야할 줄이 없다
하지만 a줄이 오름 차순인데 b줄에서 오름 차순인 부분만 실질 적으로 
다른 선하고 연결에 부딪 힘이 없기 때문에 b줄을 LIS 해서
오름차순의 수를 구하고 전체에서 그 값을 뺴주었다
'''