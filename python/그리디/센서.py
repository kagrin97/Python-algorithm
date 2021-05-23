N = int(input())
K = int(input())
road = list(map(int, input().split()))
road.sort()

if K >= N:
    print(0)
    exit()

dist = []
for i in range(1, N):
    dist.append(road[i] - road[i-1])

dist.sort(reverse=True)

for _ in range(K-1):
    dist.pop(0)

print(sum(dist))

'''
이문제는 이해하는 것부터 고난이다
n개의 센서들이 놓여있는 road에서 K개만큼 그룹을 나눈다음 그 그룹들의 거리들의
총합의 최솟값을 물어보는 문제이다
우선 K >= N일 경우 센서와 그룹의 갯수가 같으므로 그룹간의 거리가 의미없기 때문에 0을 출력한다
우선 도로를 오름차순으로 정렬을 시키고 도로간의 거리를 구한다음 내림차순으로 정렬시킨다
그리고 거리간의 수가 큰 곳부터 그룹간의 연결을 끊는다
그리고 그룹간의 거리들만 모두 합쳐주면 끝난다

'''