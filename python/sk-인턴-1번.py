def solution(p):
    n = max(p)
    answer = [0]*n

    for i in range(n):
        cut = p[i:n+1] # 현재 값부터 후에 값들까지 슬라이싱
        min_val = min(cut) # 슬라이싱된 배열중 가장 작은값
        min_idx = p.index(min_val) # 가장작은 값의 인덱스

        if i != min_idx: # 만약 현재 값 인덱스와 가장 작은 값 인덱스가 다르면
            p[i], p[min_idx] = p[min_idx], p[i] # 체인지
            answer[i] += 1 # 수정된 값의 인덱스 위치에 교체된 횟수 추가
            answer[min_idx] += 1

    return answer


p = [2, 5, 3, 1, 4]
print(solution(p))