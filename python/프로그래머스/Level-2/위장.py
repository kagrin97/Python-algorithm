from collections import Counter

def solution(clothes):
    answer = 1
    kind = []
    
    for a, b in clothes:
        kind.append(b) 
  
    kind = Counter(kind)
    # 딕셔너리 형태로 저장 Counter({'headgear': 2, 'eyewear': 1}) 

    for i in kind.values():
        answer *= (i + 1)
    # 종류1 * 종류2 = 결과 , +1 해주는 이유는 아무것도 안입는 경우도 포함
    return answer - 1
    # -1 해주는 이유는 모든 종류를 안 입는 경우도 포함한 결과기 때문에
    # 조건은 1개이상은 무조건 입기 때문에 1을 빼줌
    
clothes = [["yellow_hat", "headgear"], 
["blue_sunglasses", "eyewear"], 
["green_turban", "headgear"]]
print(solution(clothes))
