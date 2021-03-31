def solution(p, s):
    answer = []
    time = 0 # 이떄까지 지나간 시간
    count = 0 # 완료한 항목의 수
    while len(p) > 0:
        if (p[0] + time * s[0]) >= 100:
            # 100일 지났으면
            p.pop(0)
            s.pop(0)
            count += 1
            # 완료한 항목수를 늘리고 항목을 삭제한다
        else:
            if count > 0:
                answer.append(count)
                count = 0
                # 100일 지난게 없으며 완료한 항목이 있으면 추가하고 초기화
            time += 1
            # 이때까지 지나간 시간을 저장하기 위함
       
    answer.append(count) # 마지막 항목을 저장하기 위함
    return answer

progresses = [93, 30, 55]	
speeds = [1, 30, 5]
print(solution(progresses, speeds))



