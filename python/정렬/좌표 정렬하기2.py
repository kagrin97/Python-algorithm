n = int(input())

xy = []

for i in range(n):
    xy.append(list(map(int, input().split())))

xy.sort(key=lambda x: (x[1], x[0]))
# 인덱스값이 1인값부터 비교해서 정렬하는 람다식

for j in range(n):
    print(' '.join(map(str, xy[j])))
    # 괄호와 따움표를 삭제후 한줄씩 출력하는 문법
