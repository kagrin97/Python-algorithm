N, M, K = map(int, input().split()) # N, M, K 값 입력받기
array = list(map(int, input().split()))# N 개수만큼 공백 입력받기

array.sort() # 입력받은수 정렬
first = array[N-1] # 가장큰수
second = array[N-2] # 두번쨰로큰수

result = 0 

while True:
    for i in range(K): # 가장큰수 K번 더하기
        if M == 0: # M = 0이되면 종료
            break
        result += first # 큰수 더하기
        M -= 1 # 1씩 빼기
    if M == 0: # 가장 큰수 다 더하고 M이 0이되면 종료
        break
    result += second # M이 0이 아닐경우 두번쨰로 큰수 더하기
    M -= 1

print(result)