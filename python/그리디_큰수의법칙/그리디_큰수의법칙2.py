N, M, K = map(int, input().split()) # N, M, K 값 입력받기
array = list(map(int, input().split()))# N 개수만큼 공백 입력받기

array.sort() # 입력받은수 정렬
first = array[N-1] # 가장큰수
second = array[N-2] # 두번쨰로큰수

result = 0 

count = int(M / (K+1)) * K # 가장큰수가 반복되는 횟수 계산
count += M % (K+1) # 계산도중 m이k+1을 나눳을떄 딱 떨어지지 않을 경우 나머지 더하기

result = 0
result += (count) * first # 가장큰수 * 횟수 
result += (M - count) * second # 2번째큰수 * 남은횟수
 
print(result)