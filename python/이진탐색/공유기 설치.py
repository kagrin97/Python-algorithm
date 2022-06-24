import sys

N, C = map(int, sys.stdin.readline().split())
house = [int(sys.stdin.readline()) for _ in range(N)]

def router_house(mid):
    count = 1
    fir_house = house[0]
    for i in range(1, N):
        if fir_house + mid <= house[i]:
            count += 1
            fir_house = house[i]
    return count


house.sort()
start = 1
end = house[-1] - house[0]
while (start <= end):
    mid = (start + end) // 2
    if router_house(mid) >= C:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)