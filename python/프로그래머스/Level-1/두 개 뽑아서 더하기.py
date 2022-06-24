def solution(numbers):
    answer = []
    numbers.sort()
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            plus = numbers[j] + numbers[i]
            if plus not in answer: # 만약 이미 같은수가 담아져있지 않다면 더해라
                answer.append(plus)
    answer.sort() # 모든수를 오름차순으로 담으라는 요청사항이 있다(문제를 잘보자)
    return answer

n = [2,1,3,4,1]
print(solution(n))