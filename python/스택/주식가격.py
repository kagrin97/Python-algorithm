'''
프로그래머스의 스택,큐 파트에 2레벨문제 주식가격이다
'''


def solution(prices):
    answer = [0] * len(prices)  # 맨 마지막을 0으로 만들기위해 0으로 이루어진 배열 생성

    for i in range(len(prices)-1):  # 처음부터 끝까지
        for j in range(i, len(prices)-1):  # 현재 위치부터 끝까지
            if prices[i] > prices[j]:  # 현재가격보다 다음 가격이 작으면
                break  # 나감
            else:  # 가격이 떨어지지 않고 있으면 해당 위치에 값1씩 추가
                answer[i] += 1
    return answer
