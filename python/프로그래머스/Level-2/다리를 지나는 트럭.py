def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length

    while len(bridge) > 0:
        time += 1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)

    return time


bridge_length = 5
weight = 5
truck_weights = [2, 2, 2, 2, 1, 1, 1, 1, 1]
print(solution(bridge_length, weight, truck_weights))

'''
위 문제는 실제 다리를 1차원 배열로 만든 다음
다리의 무게가 오버 하지 않으면 다음 차를 들여 보내고
오버하면 0을 들여보내서 다리가 무너지지 않게 컨트롤 한다
'''



