n, k = map(int, input().split())
s = list(map(int,input().split()))  # p카드덱을 k번 d를 이용해 섞은 덱
d = list(map(int,input().split()))  # 섞는 법칙 덱

for _ in range(k):
    tmp = [0] * n
    for i in range(n):
        tmp[d[i]-1] = s[i]
    s = tmp
print(*s)

# 이 문제는 이해하는데 오래 걸린 문제이다 노트로 써가면서 해보면 됨