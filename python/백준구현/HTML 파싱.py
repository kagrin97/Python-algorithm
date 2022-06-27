html = list(input())
html = html[6:-7] # main 태그 삭제
ans = []
tmp = ""
title = ''

for i in range(len(html)):
    if tmp == '<div title="':       # 타이틀이 시작될경우
        if html[i] == '>':          # 타이틀 제목이 종료될경우
            ans.append([f'title : {title[:-1]}'])   # 제목을 문자열 마지막 (") 문자를 없애고 넣어줌
            title = ''
            tmp = ""
            continue                # title += html[i]이 실행 x
        title += html[i]

    elif tmp[:3] == '<p>':          # p태그 시작
        p_clean = ''
        flag = False

        if tmp[-4:] == '</p>':      # p태그 종료일떄
            p_all = tmp[3:-4]       # 양쪽 p태그 삭제
            for p in p_all:
                if p == '<':        # p태그 중간의 다른 잡태그, 태그값 무시
                    flag = True
                elif p == '>':
                    flag = False
                elif not flag:      # 잡태그 중간이 아니라면 문자열 추가
                    p_clean += p

            p_clean = p_clean.strip()   # 양쪽 공백제거

            while "  " in p_clean:      # 연속된 공백을 하나의 공백으로 변환
                p_clean = p_clean.replace("  ", " ")

            ans.append([p_clean])       # 깨끗해진 p태그 추가
            tmp = ""

        tmp += html[i]

    elif tmp[-6:] == '</div>':      # div 종료시 tmp초기값을 <로 설정
        tmp = "<"

    else:                           # 아무런 상태가 아닐떄 문자열 추가
        tmp += html[i]

for i in ans:
    print(*i)
