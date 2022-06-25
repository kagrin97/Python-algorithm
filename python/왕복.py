N, K = map(int, input().split())
road = list(map(int, input().split()))  # [7 4 2 4 5] 가는 도로 정보
turn_point = len(road)
revers_road = list(reversed(road))        # [5 4 2 4 7]   돌아오는 도로 정보
road = road + revers_road             # [7 4 2 4 5 5 4 2 4 7]  왕복 도로정보

for i in range(1, len(road)):
    road[i] = road[i-1] + road[i]   # [7, 11, 13, 17, 22, 27, 31, 33, 37, 44]  왕복 거리정보

for idx in range(len(road)):
    if idx < turn_point:          # 반환점을 지나기 전이라면
        if K < road[idx]:
            print(idx+1)
            exit()
    else:
        if K < road[idx]:         # 반환점을 지난후 라면
            print(turn_point-(idx-turn_point))
            exit()
