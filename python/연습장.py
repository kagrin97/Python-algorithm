from datetime import datetime, timedelta
def solution(m, musicinfos):
    m = m.replace('A#','H')
    m = m.replace('C#','I')
    m = m.replace('D#','J')
    m = m.replace('F#','K')
    m = m.replace('G#','L')
    m = m.replace('E#','Q')
    answer = []
    mu_list = []
    max_time = 0
    for i in musicinfos:
        mu_info = i.split(',')
        for _ in range(1):
            s_t = mu_info[0].split(':')
            e_t = mu_info[1].split(':')
            time = 60 * (int(e_t[0])-int(s_t[0])) + (int(e_t[1])-int(s_t[1]))
            print(time)
            melody = []
            one_str = mu_info[3]
            one_str = one_str.replace('A#','H')
            one_str = one_str.replace('C#','I')
            one_str = one_str.replace('D#','J')
            one_str = one_str.replace('F#','K')
            one_str = one_str.replace('G#','L')
            one_str = one_str.replace('E#','Q')                       
            while len(melody) < time:
                for j in one_str:
                    if len(melody) == time:
                        break
                    else:
                        melody.append(j)
            
            if "".join(list(m)) in "".join(melody):
                mu_list.append([mu_info[2],time])
                max_time = max(max_time, time)

    if not mu_list:
        return '(None)'

    for n, t in mu_list:
        if max_time == t:
            answer.append(n)


    return answer[0]
m = "CDEFGAC"
musicinfos = ["12:00,13:06,HELLO,CDEFGA"]
print(solution(m, musicinfos))