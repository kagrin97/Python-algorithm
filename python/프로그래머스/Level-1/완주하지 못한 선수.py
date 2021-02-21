def solution(participant, completion):
    participant.sort()# 같은 이름끼리 묶기위한 정렬
    completion.sort()
    
    for p, c in participant, completion:# 둘이 더해주고 나눠줌
        if p != c:
            return p # 완주하지 못하면 p 리턴
    
    return participant[-1]
# 여러명이 완주를 못했으면 1명만 완주하지못했다는 조건을 만족x 라서 맨 마지막을 출력

s = ["marina", "josipa", "nikola", "vinko", "filipa"]
n = ["josipa", "filipa", "marina", "nikola"]
print(solution(s,n))