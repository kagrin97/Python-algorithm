import datetime

def solution(a, b):
    answer = ''
    days = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    answer = days[datetime.date(2016, a, b).weekday()]
    # 요일을 구해주는 라이브러리
    return answer

a = 5
b = 24
print(solution(a, b))