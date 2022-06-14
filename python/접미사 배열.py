string = list(input())
ans = []

for i in range(len(string)):
    tmp = ""
    for j in range(i, len(string)):
        tmp += string[j]
    ans.append(tmp)

ans = sorted(ans)

for i in ans:
    print(i)




