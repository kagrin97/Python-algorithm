def solution(skill, skill_trees):
    answer = 0

    for i in skill_trees:
        skill_list = list(skill)
        # CBD를 리스트 형태로 저장 ["C", "B", "D"]
        for s in i:
            if s in skill:
                # skill_trees안의 값이 cbd 중 하나라면
                if s != skill_list.pop(0):
                    break
                # 첫번째 값을 뺌과 동시에 스킬 트리를 확인 
                # 순서가 맞지 않으므로 나옴
        else:
            answer += 1
            # skill_trees값이 skill안에 아예 없을 경우 1 추가

    return answer

p = "CBD"	
l = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(p,l))



