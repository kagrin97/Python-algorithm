'''
파이썬 브루트포스 덩치
'''

n = int(input())
xy = []

for i in range(n):
    xy.append(list(map(int, input().split())))
    #  n명에게 몸무게, 키를 받아서 리스트 형태로 xy에 추가

for j in xy:
    rank = 1
    # rank에서 가장 높은 값이 1이여서 1을 넣어줌
    for k in xy:
        if j[0] < k[0] and j[1] < k[1]:
            rank += 1
            # 현재 값과 뒤에 모든 값을 비교해서 하나라도 크면 랭크를 다운시킴

    print(rank, end=" ")
    # 현재 값의 랭크값과 공백을 출력
