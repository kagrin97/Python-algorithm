N, L = map(int, input().split())
water = list(map(int, input().split()))
water.sort()

tape = 1
start = water[0]
end = start + L - 0.5 # 0.5만큼의 간격을 줘야함

for i in water:
    if end >= i: # 현재 테이프안 이라면 
        continue 
    else: # 테이프보다 길다면 테이프를 하나 더씀 그리고 테이프값을 갱신
        tape += 1
        end = i + L - 0.5

print(tape)
