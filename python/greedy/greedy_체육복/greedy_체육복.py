'''
이 문제는 함정이 있는데 도난당한 학생과 여벌이 있는 학생이 중복이 없다는 것은
이문제는 집합을 이용해야 한다는 점이다 . 
그리고 잃어버리고 여벌이 있는 학생의 경우 아예 제외를 시킨다는 점이다
또 왼쪽 학생부터 빌려줘야지 체육복을 가진 인수가 최대로 늘릴수 있어서 왼쪽부터 빌려준다
'''


def solution(n, lost, reserve):
    reserve_set = set(reserve) - set(lost)
    # 읽어버렸지만 여벌이 있는 학생을 제외 하기 위해서 빌려 줄수있는 학생을 구하고
    lost_set = set(lost) - set(reserve)
    # 여벌이 있지않고 순전히 잃어 버린 학생을 구하기 위해 집합끼리 뺴서 차집합을 구하고
    for i in reserve_set:
        # 빌려 줄수있는 학생이 없을경우 반복문을 종료 시킨다.
        if i-1 in lost_set:  # 만약 왼쪽 학생이 잃어 버렸을경우
            lost_set.remove(i-1)  # 빌려줬다 치고 왼쪽학생을 잃어버린 명단에서 제외
        elif i+1 in lost_set:  # 오른쪽 학생이 잃어 버렸을경우 명단에서 제외
            lost_set.remove(i+1)

    return n - len(lost_set)
    # 총 인원에서 결국 잃어버리고 빌리지 못한 학생을 뺌
