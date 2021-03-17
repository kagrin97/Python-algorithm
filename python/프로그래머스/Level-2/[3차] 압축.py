def solution(msg):
    Dict = dict()
    for i in range(65, 91):
        Dict[chr(i)] = i - 64 
        # 사전에 각 단어와 색인을 넣어줌
    start = 0
    end = len(msg)
    r = [] # 정답용

    while True:
        a = msg[start:end]
        if a in Dict.keys():
            r.append(Dict[a])
            if end >= len(msg): # 마지막까지 실행되면 종료
                return r
            Dict[a+msg[end]] = max(Dict.values())+1 # KA값을 가장큰값+1로 저장
            start += len(a) # 그다음 문자 검사를 위함
            end = len(msg)
        else:
            end -= 1
            # 사전에 일치하는 문자가 없을경우 문자를 좁힘

msg = "KAKAO"
print(solution(msg))