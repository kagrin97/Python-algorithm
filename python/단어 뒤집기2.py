s = list(input())
tmp = ''
ans = []
tag = False

for i in s:
    if i == '<':
        if tmp:
            ans.append(tmp[::-1])
        tmp = ''
        tmp += i
        tag = True
    elif i == '>':
        tmp += i
        ans.append(tmp)
        tmp = ''
        tag = False
    elif tag:
        tmp += i
    elif i == " ":
        ans.append(tmp[::-1])
        ans.append(" ")
        tmp = ""
    elif not tag:
        tmp += i
if tmp:
    ans.append(tmp[::-1])

print("".join(ans))