a, b = map(int, input().strip().split(' '))
s = ""
for i in range(a*b):
    s += "*"

    
for i in range(b):
    print()
    for j in range(a):
        print(s[j], end="")





