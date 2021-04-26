def change_int(time):
    t = int(time[:2]) * 3600
    m = int(time[3:5]) * 60
    s = int(time[6:])
    return t+m+s

def change_time(answer):
    t = answer // 3600
    answer -= t * 3600
    m = answer // 60
    answer -= m * 60

    if t < 10:
        t = f'0{t}'
    if m < 10:
        m = f'0{m}'
    if answer < 10:
        answer = f'0{answer}'
    return f'{t}:{m}:{answer}'

def solution(play_time, adv_time, logs):
    dp = [0] * (change_int(play_time) + 1)

    for i in logs:
        temp = i.split('-')
        start = change_int(temp[0])
        end = change_int(temp[1])
        dp[start] += 1 
        dp[end] -= 1

    for i in range(1, change_int(play_time)):
        dp[i] = dp[i] + dp[i-1]
    for i in range(1, change_int(play_time)):
        dp[i] = dp[i] + dp[i-1]
    max_value = -1
    answer = 0
    for i in range(change_int(adv_time)-1, change_int(play_time)):
        temp = dp[i] - dp[i-change_int(adv_time)]
        if temp > max_value:
            max_value = temp
            answer = i-change_int(adv_time) + 1

    return change_time(answer)

play_time = "02:03:55"	
adv_time = "00:14:15"	
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29",
 "01:30:59-01:53:29", "01:37:44-02:02:30"]

print(solution(play_time, adv_time, logs))

''' 
이 문제는 처음에 그리디로 풀어봤는데 답은 맞지만 시간초과가 나왔고
결국 잘 모르겠어서 https://bladejun.tistory.com/72 이 사이트를 참고했다
31 ~ 34 줄은 dp형식으로 start와 end값이 많이 중복되어 +=, -= 된곳이 많은
시청자가 모여있는 곳이기 때문에 dp에서 시작과 끝지점 차이가 가장 큰 곳이 (37~41줄)
시청자가 가장 많이 모여있는 시간대이다
'''