n = int(input())
check = True
s = n+3

for i in range(1, 2*n):
    if check:
        print(i*'*' + s*' ' + i*'*')
        s -= 2
        if i == n:
            check = False
            s = 2
            j = n-1
    else:
        print(j*'*' + s*' ' + j*'*')
        s += 2
        j -= 1




    



    




