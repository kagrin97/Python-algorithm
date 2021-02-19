def solution(n, stages):
    result = {}
    num_people = len(stages)
    for i in range(1, n + 1):
        if num_people != 0:
            count = stages.count(i)
            result[i] = count / num_people
            num_people -= count
            # 딕셔너리로 스테이지마다 실패율울 넣어줌
        else:
            result[i] = 0
            # 도달한 사람이 없으면 0을 딕셔너리에 넣어줌

    return sorted(result, key=lambda x : -result[x])
    # value값을 기준으로 정렬한 key 리스트를 반환해 준다 내림차순은 -를 붙임
n = 5
a1 = [2, 1, 2, 6, 2, 4, 3, 3]	
print(solution(n, a1))





