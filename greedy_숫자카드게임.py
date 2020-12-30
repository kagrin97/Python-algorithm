''' 
1. 숫자 카드들이 n x m 형태로 있음
2. 먼저 뽑고자 하는 행을 선택
3. 선택된 행에 가장 낮은 숫자 카드를 뽑음
4. 모든 행에서 가장 낮은 숫자들중 가장 큰수를 출력 하라
'''



n, m = map(int, input().split()) # n = 행 m = 열

result = 0 

for i in range(n): # 행 만큼의 값들을 받음
    value = list(map(int, input().split())) # 각 행마다 열값을 받음
    min_value = min(value) # 각 열에 작은 값을 저장
    
    result = max(result, min_value) # 작은 값들중에 큰값을 결과에 저장

print(result)