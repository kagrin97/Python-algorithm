N, K = map(int, input().split())
array = [i for i in range(1, N+1)]
result = []
temp = K-1 # 찾고자하는 위치

for i in range(N):
    if len(array) > temp: # 찾고자하는 위치가 범위안이면 넣고 빼줌
        result.append(array.pop(temp))
        temp += K-1 # array에 값하나를 뺏기때문에 -1을 해줘야 제대로 돌아감
    elif len(array) <= temp: # 찾고자하는 위치를 넘을 경우
        temp %= len(array) # 전체 길이에서 나눈 나머지를 넣어줌
        result.append(array.pop(temp))
        temp += K-1 
        
print('<', end='')
for i in result:
    if i == result[-1]:
        print(i, end='')
    else:
        print(i, end=", ")
print('>')