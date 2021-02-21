def get_near_hand(position, l, r, num, hand):
    left_distance = abs(position[l][0] - position[num][0]) + abs(position[l][1] - position[num][1])
    right_distance = abs(position[r][0] - position[num][0]) + abs(position[r][1] - position[num][1])
    # 중간에 있는 값들과의 위치를 구하기위해 포지션에서 재위치 값을 각각주고 절대값으로 더해주면 거리가 나온다
    # 현재 8.(2, 1), 이동후 #.(3, 2) -> abs(2-3) + abs(1-2) = 2 즉 거리는 2로 결론이 나온다    

    if left_distance == right_distance:
        if hand == "left":
            near_hand = "L"
        else:
            near_hand = "R"
    else :
        if left_distance < right_distance:
            near_hand = 'L'
        else:
            near_hand = 'R'
    return near_hand

def solution(numbers, hand):
    left_key = [1, 4, 7]
    right_key = [3, 6, 9]
    hand_positions = ["*", "#"]

    position = {
        1: (0, 0), 2: (0, 1), 3:(0, 2),
        4: (1, 0), 5: (1, 1), 6:(1, 2),
        7: (2, 0), 8: (2, 1), 9:(2, 2),
        "*": (3, 0), 0: (3, 1), "#":(3, 2),
    }
    answer = ''

    for num in numbers:
        if num in left_key:
            # 누를 키가 left_key에 있을떄 값에 l을 넣고 포지션을 num값으로 갱신
            answer += "L"
            hand_positions[0] = num
        elif num in right_key:
            # 누를 키가 right_key에 있을떄 값에 r을 넣고 포지션을 num값으로 갱신
            answer += "R"
            hand_positions[1] = num
        else:
            near_hand = get_near_hand(position, hand_positions[0], hand_positions[1], num, hand)
            if near_hand == "L":
                answer += "L"
                hand_positions[0] = num
            else:
                answer += "R"
                hand_positions[1] = num
                # 따로 함수를 빼서 중간에 있는 키(2,5,8,0) 들으 계산후 비교후 갱신및 값을 추가

    return answer 

n = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
h = "right"
print(solution(n,h))

'''
위 문제는 구현 문제이다 
이런 문제를 풀때는 전체적인 틀을 만들 코드를 다 짜두고 세세하게 하는 편이 좋은 것 같다
'''



