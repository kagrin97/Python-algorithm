def solution(skill, skill_trees):
    answer = 0

    for i in skill_trees:
        skill_list = list(skill)
        

        for s in i:
            if s in skill:
                if s != skill_list.pop(1):
                    print(skill_list)
                    break
        else:
            answer += 1

    return answer

p = "CBD"	
l = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(p,l))



