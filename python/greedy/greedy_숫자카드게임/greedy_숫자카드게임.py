n, m = map(int, input().split()) # n = 행 m = 열

result = 0 

for i in range(n): # 행 만큼의 값들을 받음
    value = list(map(int, input().split())) # 각 행마다 열값을 받음
    min_value = min(value) # 각 열에 작은 값을 저장
    
    result = max(result, min_value) # 작은 값들중에 큰값을 결과에 저장

print(result)