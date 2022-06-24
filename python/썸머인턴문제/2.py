def solution(t, r):
    answer = []
    s = []
    for i in range(len(t)):
        s.append([t[i], r[i], i])
    s = sorted(s, key = lambda x : x[0], x[1], x[2])
    idx = 0
    tmp = []
    
    while idx != len(t):
        for i in range(len(s)):
            if s[i][0] <= idx:
                tmp.append([s[i]])
        
        print(tmp)


        idx += 1


                    
        
   
        

    return s


t = [0,1,3,0]	
r = [0,1,2,3]
print(solution(t, r))