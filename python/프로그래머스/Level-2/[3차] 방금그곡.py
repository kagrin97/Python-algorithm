def solution(m, musicinfos):
    m = m.replace('A#','H')
    m = m.replace('C#','I')
    m = m.replace('D#','J')
    m = m.replace('F#','K')
    m = m.replace('G#','L')
    m = m.replace('E#','Q') #  #을 계산 하기 쉽게 다른 알파벳으로 바꿔준다
    answer = []
    mu_list = [] # 제목과 재생시간을 넣는 곳
    max_time = 0 # 최대 재생 시간
    for i in musicinfos:
        mu_info = i.split(',')
        for _ in range(1):
            s_t = mu_info[0].split(':') # ['12', '24'] 시간, 분으로 저장
            e_t = mu_info[1].split(':')
            time = 60 * (int(e_t[0])-int(s_t[0])) + (int(e_t[1])-int(s_t[1]))      
            melody = [] # 재생시간동안 연주된 음표 리스트
            one_str = mu_info[3] # 디폴트 음표 리스트
            one_str = one_str.replace('A#','H') # 마찬가지로 계산하기 쉽게 변환
            one_str = one_str.replace('C#','I')
            one_str = one_str.replace('D#','J')
            one_str = one_str.replace('F#','K')
            one_str = one_str.replace('G#','L')
            one_str = one_str.replace('E#','Q')                       
            while len(melody) < time: # 만약 재생시간보다 멜로디가 길어지면 종료
                for j in one_str:
                    if len(melody) == time: # 재생시간과 멜로디가 같으면 종료
                        break
                    else:
                        melody.append(j) 
            
            if "".join(list(m)) in "".join(melody): # 찾고자하는 멜로디가 melody리스트에 있을경우
                mu_list.append([mu_info[2],time]) # 제목과 재생시간을 넣어줌
                max_time = max(max_time, time) # 조건충족을 위한 최대 재생시간 갱신

    if not mu_list:
        return '(None)'

    for n, t in mu_list: # 최대 재생시간과 현재 곡의 재생시간이 일치하면 제목을 저장
        if max_time == t:
            answer.append(n)

    return answer[0] # 제일앞에오는 곡이 제일처음으로 재생된 곡
m = "CC#BCC#BCC#BCC#B"
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]	
print(solution(m, musicinfos))

'''
위문제는 2가지 고비가 있었는데 C#같이 반음을 고려를 하지 못 했던점과
처음에는 단순히 시간을 1404 - 1304 처럼 뺄려고 하니까 minute 60과 정수 100과의 차이를 생각
하지 못했던 점이 고비였다 
해결방법은 시간만을 뺴고 난 값에 * 60을 해주면 minute이 나온다 14시 - 13시 = 1시간 , 
1시간 * 60 = 60분 
'''
