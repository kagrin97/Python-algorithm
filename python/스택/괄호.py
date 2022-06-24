N = int(input())
def check(bra):
    stack=[]
    for i in bra:
        if i == "(":
            stack.append(i)
        else :
            if not stack:
                print("NO")
                return
            else :
                stack.pop()               
    if not stack:
        print("YES")
        return
    else : 
        print("NO")
        return

for _ in range(N):
    s = input()
    check(s)