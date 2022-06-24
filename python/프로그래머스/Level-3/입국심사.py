def solution(n, times):
    answer = 0
    leng = len(times)
    left = 1
    right = (leng+1) * max(times) # 10분씩 3번 총 6명이 받는 최대시간

    while left <= right:
        mid = (left + right) // 2 # 한명의 심사위원이 감당할 시간

        count = 0
        for time in times:
            count += mid // time # count는 감당할수있는 인원수
            if count >= n: # 모든인원을 시간내에 감당할수 있으면 종료
                break
        
        if count >= n: # 모든인원을 감당할수 있으면
            answer = mid # 감당가능 시간을 갱신
            right = mid - 1 # 최대 값을 줄여줌

        elif count < n: # 감당할수가 없으면
            left = mid + 1 # 최소 값을 높여서 mid값을 올려줌

    return answer

n = 6       
times = [7, 10]
print(solution(n, times))

'''
최소시간과 최대시간을 구한뒤 mid값을 구한다 mid값은 
한명의 심사위원이 감당할 시간으로 만약 시간내에 모든인원을 완료하지
못한다면 감당할 시간을 더 늘린다 만약 모든 인원을 완료할수있으면
최적의 시간을 찾기위해 감당할 시간을 줄여준다
'''

