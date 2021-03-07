def solution(dirs):
    command = {'U':(0, 1), 'D':(0, -1), 'L':(-1, 0), 'R':(1, 0)} # 4방향 설정
    road = set() # 중복방지 set (왔던길을 없애기위함)
    cur_x, cur_y = (0,0) # 초기 위치

    for d in dirs:
        next_x, next_y = cur_x + command[d][0], cur_y + command[d][1] # 다음 위치의 x,y를 구함
        if -5 <= next_x <= 5 and -5 <= next_y <= 5: # 실행이 되면
            road.add((cur_x, cur_y, next_x, next_y)) # 가는길
            road.add((next_x, next_y, cur_x, cur_y)) # 돌아가는길
            # 가는길, 돌아가는길 두개를 더한 이유는 가는 길을 저장도 하지만 다시 돌아가는 길도 저장을 해야지
            # 되돌아가는 경우를 다시 또 추가하지 못하게 하기 위함이다
            cur_x, cur_y = next_x, next_y
    
    return len(road) // 2
    # 2개씩 저장을 하기때문에 //2를 해줌

b = "ULURRDLLU"
print(solution(b))