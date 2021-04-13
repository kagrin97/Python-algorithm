m = int(input())
n = int(input())
per = []

for i in range(m, n+1):
    if int(i**0.5) ** 2 == i: # 완전 제곱수를 판별한다
        per.append(i)

if per:
    print(sum(per))
    print(min(per))
else:
    print(-1)

'''
완전 제곱수란 제곱이되는수인 1,4,9,16 중에서
약수가 홀수개인 9(1,3,9) 등을 말한다
'''