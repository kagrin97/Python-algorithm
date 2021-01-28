n = int(input())
coin = list(map(int, input().split()))
coin.sort() # 정렬
target = 1 # 타겟을 현재 조합해서 만들수있는 금액

for i in coin: # 동전 수만큼 반복
    if target < i: # 만들수없는 금액을 만들었을떄 종료
        break
    target += i

print(target)