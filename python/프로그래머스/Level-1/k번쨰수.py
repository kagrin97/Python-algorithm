def solution(array, commands):
    answer = []
    for i in range(len(commands)): 
        data = [] # 초기화
        data.append(array[(commands[i][0]) - 1:commands[i][1]]) # 숫자를 자를 구간 정하기 0부터 시작이니 1감소
        data = sum(data, []) # 리스트 한 겹 벗기기
        data.sort() 
        answer.append(data[(commands[i][2]) - 1]) # [i][2]번째 자리 숫자를 구함 0부터 시작이니 1감소

    return answer


s = [1, 5, 2, 6, 3, 7, 4]
n = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(s, n))