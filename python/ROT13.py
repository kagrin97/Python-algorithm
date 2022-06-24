string = list(input())
ans = []
for s in string:
    if s.isupper():
        if 65 <= ord(s) <= 77:
            a = chr(ord(s) + 13)
            ans.append(a)
        elif 77 <= ord(s) <= 90:
            a = chr(65 + (ord(s) - 78))
            ans.append(a)
    elif s.islower():
        if 97 <= ord(s) <= 109:
            a = chr(ord(s) + 13)
            ans.append(a)
        elif 109 <= ord(s) <= 122:
            a = chr(97 + (ord(s) - 110))
            ans.append(a)
    else:
        ans.append(s)

print("".join(ans))




