def shopping(gems):
    start, end = 0, 0 # 투 포인터
    gem_num = len(set(gems)) # 최소 요구치 보석의 양
    gem_dict = {gems[0]: 1} # 초기값 
    result = (0,100001) # start최소값, end최대값
    
    while start < len(gems) and end < len(gems): # 두 포인터가 끝까지 갈때까지
        if len(gem_dict) < gem_num: # 최소 요구치를 충족못했을때
            if end == len(gems) - 1: # end가 끝까지 갔을시 종료
                break
            end += 1 # end 증가
            if gem_dict.get(gems[end]) is None: # dic안에 해당 보석이 없을 경우
                gem_dict[gems[end]] = 1 # 해당 보석을 생성과 기본값 1
            else:
                gem_dict[gems[end]] += 1 # 해당 보석 갯수 추가
        else:
            if end - start < result[1] - result[0]: # 범위가 전에 구한 범위보다 작을경우
                result = (start+1, end+1) # 갱신(dic은 인덱스가 0부터 시작해서 +1해줌)
            if gem_dict[gems[start]] == 1: # start위치의 보석 개수가 1일경우 없애줌
                del gem_dict[gems[start]]
            else:
                gem_dict[gems[start]] -= 1 # start위치의 보석의 개수를 줄여줌
            start += 1 # start 증가
    return result
            
def solution(gems):
    answer = shopping(gems)
    
    return list(answer) # 변환

gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))

'''
이 문제는 투포인터를 이용한 문제로
start와 end를 이용해서 최소 요구치의 보석의 양의 만족하는 범위를 생성하고 (8~15줄)
start 값을 늘리면서 최소범위를 구하기위해 보석을 하나씩 빼준다 (중간중간 범위를 저장한다 16~23줄)
보석을 줄이다가 최소 요구치를 만족을 못했을시에는 다시 보석을 추가해준다
이 과정을 반복하다가 두 포인터가 끝에 도달했을때 종료한다
'''
