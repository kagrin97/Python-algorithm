from copy import deepcopy
def solution(stones, k):
    answer = 0
    start = 0
    end = 200000000 

    while start <= end:
        mid = (start + end) // 2
        count = 0
        check = False

        tmp = deepcopy(stones)
        for i in range(len(tmp)):
            tmp[i] -= mid # 현재 인원수에 맞게 징검다리 숫자를 줄여줌
        
        for t in range(len(tmp)):
            if tmp[t] <= 0:
                count += 1
            else:
                count = 0
        
            if count >= k: # 건널수가 없을때
                check = True
                break
        
        if check:
            answer = mid # 건널수 없으니 인원수를 더 줄임
            end = mid - 1
        else:
            start = mid + 1
        
    return answer   

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(stones, k))


