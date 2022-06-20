def change(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    return change(q, base) + T[r] if q else T[r] # 진법 변환 함수

def solution(n, t, m, p):
    total_num = '' # 총 인원수 * 구할 숫자의 갯수 = 만큼의 문자열을 구해줌
    start = 0
    ans = ''
    while 1:
        a = change(start, n) # 진법 변환
        total_num += a # 변환된 숫자를 넘어줌
        start += 1      # 변환시킬 다음 숫자
        if len(total_num) > t * m: # 총 인원수 * 구할 숫자의 갯수를 넘기면 종료
            break

    for i in range(p - 1, len(total_num), m): # 본인차례의 숫자를 구해줌
        ans += total_num[i]
    return ans[:t] # 말해야하는 숫자수만큼 잘라줌


n = 16
t = 16
m = 2
p = 2
print(solution(n, t, m, p))