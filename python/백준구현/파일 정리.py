n = int(input())
extension = {}          # 확장자 모음
for i in range(n):
    _, ex = input().split(".")
    if ex in extension:
        extension[ex] += 1
    else:
        extension[ex] = 1

extension = sorted(extension.items(), key=lambda x:x[0])    # 확장자 사전순 정렬

for i in extension:
    print(i[0], i[1])