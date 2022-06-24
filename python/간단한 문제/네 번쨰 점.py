x = []
y = []
for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

for i in x:
    if x.count(i) == 1:
        q = i
        break
for i in y:
    if y.count(i) == 1:
        w = i
        break
    
print(q, w)






    



    




