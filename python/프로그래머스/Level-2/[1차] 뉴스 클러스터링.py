def solution(str1, str2):
    s1=[str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    s2=[str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]

    gyo = 0
    hap = 0

    for s in set(s1+s2):
        hap += max(s1.count(s), s2.count(s))
        gyo += min(s1.count(s), s2.count(s))

    if hap == 0:
        return 65536
    else: 
        return int(gyo/hap * 65536)

str1 = "FRANCE"
str2 = 'french'
print(solution(str1, str2))