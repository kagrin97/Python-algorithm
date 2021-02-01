n = int(input())

ugly = [0] * n
ugly[0] = 1

i2 = i3 = i5 = 0
# 다음 배수를 위한 인덱스 
next2, next3, next5 = 2, 3, 5
# 처음 곱셈 값 초기화

for i in range(1, n):
    ugly[i] = min(next2, next3, next5)
    # 순서대로 작은 수부터 할당(next 값이 계속 증가됨)
    if ugly[i] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
        # 값이 next2 일경우 인덱스를 이용해 다음 next2 값으로 재 할당
    if ugly[i] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[i] == next5:
        i5 += 1
        next5 = ugly[i5] * 5
    
print(ugly[n - 1])