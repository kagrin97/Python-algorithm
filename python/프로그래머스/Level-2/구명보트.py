from collections import deque

def solution(people, limit):
    count = 0
    people.sort()
    people = deque(people)

    while people:
        if len(people) == 1:
            count += 1
            break
        if (people[0] + people[-1]) <= limit:
            try:
                people.popleft()
                people.pop()
                count += 1
            except:
                break
        else:
            people.pop()
            count += 1

    return count

people = [70, 50, 80, 50]
limit = 100
print(solution(people, limit))

'''
구명보트 문제는 오름차순으로 정렬후 맨앞과 맨뒤값을 더한값이 limit보다
작거나 같을때 둘다 큐에서 빼주고 limit보다 크면 맨뒤 값만 빼준다
'''
