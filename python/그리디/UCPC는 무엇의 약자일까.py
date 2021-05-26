s = ['C', 'P', 'C', 'U']
ucpc = input()

for i in range(len(ucpc)):
    
    if ucpc[i] == s[-1]:
        s.pop()
    if not s:
        print("I love UCPC")
        exit()

print("I hate UCPC")

