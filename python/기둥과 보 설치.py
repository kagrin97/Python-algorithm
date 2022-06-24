def check(a):
    for x, y, what in a:
        if what == 0: # 기둥설치
            if y == 0 or [x-1, y, 1] in a or [x, y, 1] in a or [x, y-1, 0] in a:
                # 바닥에 설치 or 왼쪽이나오른쪽에 보가 설치 or 밑에 기둥이 있으면 설치가능
                continue
            else:
                return False # 설치가 안되면 false 리턴
        elif what == 1: # 보 설치
            if [x, y-1, 0] in a or [x+1, y-1, 0] in a or ([x-1, y, 1] in a and [x+1, y, 1] in a):
                # 보 밑에 기둥이존재 or 보 오른쪽끝에 기둥이존재 or (왼쪽오른쪽 둘다 보가 존재 하면 설치) 
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    answer = []

    for x, y, what, how in build_frame: 
        if how:
            answer.append([x, y, what])
            if not check(answer): # 설치할수 없을때는 리스트에서 삭제
                answer.remove([x, y, what])
        else:
            answer.remove([x, y, what]) # 지우고나서 함수가 오류가 나면 다시 넣어줌
            if not check(answer):
                answer.append([x, y, what])

    answer.sort() # 정렬

    return answer

n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],
[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

print(solution(n, build_frame))