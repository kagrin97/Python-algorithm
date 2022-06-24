import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    point = []
    for _ in range(n):
        point.append(list(map(int, input().split())))
    point.sort(key=lambda x:x[0]) # 서류 심사성적으로 오름차순 정렬
    cnt = 1 # 통과된 인원
    min_val = point[0][1] # 면접성적의 기준값
    
    for i in range(1, n):
        if point[i][1] < min_val: # 면접점수가 0번쨰 사람보다 낮으면
            cnt += 1 # 통과됨(왜냐하면 1나라도 더 낮은 점수가 존재하기 때문)
            min_val = point[i][1] # 더 낮은 점수 갱신

    print(cnt)
