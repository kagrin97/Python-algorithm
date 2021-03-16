from itertools import combinations as combi
def solution(relation):
    row = len(relation)
    col = len(relation[0])

    mix_combi = []
    for i in range(1, col+1):
        mix_combi.extend(combi(range(col),i)) # 조합을 구함
        # extend는 append와 달리 객체를 받으면 풀어서 저장한다 
        # append => <itertools.combinations object at 0x0000016FD01BA810>
    unique = []
    for mix in mix_combi:
        tmp = [tuple([item[i] for i in mix]) for item in relation] #각 조합에 따라 relation을 만듦
        if len(set(tmp)) == row: # 길이가 같지않으면 중복이 있어 삭제됨(즉 유일성x)
            unique.append(mix)

    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)): # 현재와 그다음 모든 값들을 검사
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])
            # 길이가 같다는 것은 같은 길이의 값들이 있으므로 제거
            # discard는 remove와 달리 KeyError가 발생하지 않음
    return len(answer)

relation = [["100","ryan","music","2"],
            ["200","apeach","math","2"],
            ["300","tube","computer","3"],
            ["400","con","computer","4"],
            ["500","muzi","music","3"],
            ["600","apeach","music","2"]]
print(solution(relation))

'''
이 문제는 전체 조합을 구하고 [0], [0,1] ...
유일성을 검사한다 즉 각조합에 따른 relation값에 중복이 없어야함
그리고 최소성을 검사한다 현재 값과 교집합(현재+그다음) 의 길이가 같다면
교집합 결과 현재와 그다음이 똑같기 때문에 중복이라 그값을 삭제함
''' 