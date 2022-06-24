def solution(n, results):
    win, los = {}, {} 

    for i in range(1, n+1):
        win[i], los[i] = set(), set() #({1: {2, 5}, 2: {5}) 딕셔너리안에 set을 적용
    
    for i in range(1, n+1):
        for r in results:
            if r[0] == i:
                win[i].add(r[1]) # i에게 진사람들 
            if r[1] == i:
                los[i].add(r[0]) # i에게 이긴 사람들
        
        for w in los[i]:
            win[w].update(win[i]) # w가 무조건 이길수 있는 사람들
        for l in win[i]:
            los[l].update(los[i]) # l이 무조건 지는 사람들
    
    count = 0
    for i in range(1, n+1):
        if len(win[i]) + len(los[i]) == n-1: # 자신을 제외한 모두와의 싸움 결과를 알수 있을때
            count += 1 

    return count

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results))

'''
이문제는 이해하기가 어려웠지만 예를 들어 1번은 2번을 이겼다, 2번은 5번을 이겼다
다음 같은 논리로 1번과 5번을 싸우진 않았지만 무조건 이길수 있다가 성립이 된다 (14~17번쨰 줄) 
그리고 win데이터 + los데이터 = 나를 제외한 모두가 성립할때 자신의 순위를 정확하게 알수 있다
'''
