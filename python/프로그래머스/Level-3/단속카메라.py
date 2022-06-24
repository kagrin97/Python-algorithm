def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1]) # 나간 기준으로 오름차순 정렬
    camera = -30001 # 최하위치로 초기화

    for route in routes:
        if camera < route[0]: # 카메라가 진입지점보다 적으면
            answer += 1     # 해당차량을 카메라로 포착을 못했기때문에 카메라 늘림
            camera = route[1] # 카메라의 위치를 해당지점의 나간위치를 기준으로 갱신
    return answer

routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes))
