ID = dict() # ID값과 이름을 키와 값으로 저장함
def solution(record):
    answer = []
    tmp = [] # 임시로 ID와 text를 저장하는 곳
    for e in record:
        data = e.split(" ") # 공백을 기준으로 행위, id, 닉네임을 따로 저장
        if 'L' in data[0]: 
            tmp.append([data[1], "님이 나갔습니다."])          
        elif 'E' in data[0]:
            tmp.append([data[1], "님이 들어왔습니다."])
            ID[data[1]] = data[2] # 들어갈때 id와 이름을 저장
        elif 'C' in data[0]:
            ID[data[1]] = data[2] # 해당 id값을 모두 새로 바꿔줌

    for t in tmp:
        answer.append(ID[t[0]]+t[1]) 
        # 딕셔너리에서 id값으로 이름을 불러오고 t로 text를 합쳐줌
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo",
"Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))