def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    arr1 = []
    arr2 = [] 개그튼거

    for i in range(len(str1)):
        try:
            if not str1[i].isalpha():
                str1 = str1[:i] + str1[i+1:]
            if not str1[i+1].isalpha():
                str1 = str1[:i+1] + str1[i+2:]
            else:
                arr1.append(str1[i]+str1[i+1])
        except:
            pass
    
    for i in range(len(str2)):
        try:
            if not str2[i].isalpha():
                str2 = str2[:i] + str2[i+1:]
            if not str2[i+1].isalpha():
                str2 = str2[:i+1] + str2[i+2:]
            else:
                arr2.append(str2[i]+str2[i+1])
        except:
            pass
    gyo, hap = 0, 0
    for s in set(arr1 + arr2):
        hap += max(arr1.count(s), arr2.count(s))
        gyo += min(arr1.count(s), arr2.count(s))

    if hap == 0:
        return 65536
    else:
        return int(gyo / hap * 65536)

    

n =	"AAbbaa_AA"
a = "BBB"
print(solution(n, a))