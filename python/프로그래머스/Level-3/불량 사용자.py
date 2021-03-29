from itertools import permutations

def check(user_set, banned_set):
    for i in range(len(user_set)):
        if len(user_set[i]) != len(banned_set[i]): # 양쪽 글자수가 다르면 다른글자 이기때문에 종료
            return False
        for j in range(len(user_set[i])): # 글자수 만큼 반복
            if banned_set[i][j] == '*': # *이면 통과
                continue
            if user_set[i][j] != banned_set[i][j]: # 다르면 종료
                return False
    return True # 모든 글자를 비교해도 이상없으면 반납

def solution(user_id, banned_id):
    answer=[]

    for user_set in permutations(user_id, len(banned_id)): # ('abc123', 'fradi'), ('abc123', 'crodo') 이런식으로 조합
        if check(user_set, banned_id): # user_set 조합하고 banned_id하고 비교하는 함수
            user_set = set(user_set) # 비교할 리스트를 set으로 바꾸면 비교당할 리스트에서 중복을 검색할 수 있다
            if user_set not in answer: # 중복검사시 중복이 아니라면 추가
                answer.append(user_set)
    return len(answer)

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]
print(solution(user_id, banned_id))

'''
이문제는 19번줄 set이 핵심인데 set으로 문자열을 넣을 경우 ('frodo', 'crodo', 'abc123')와 ('crodo', 'frodo', 'abc123')
을 같은 문자열로 인식을 한다 즉 answer안에있는 튜플들은 모두 set의 속성을 가지고 있다(넣을때 set으로 넣었기 때문이다)
