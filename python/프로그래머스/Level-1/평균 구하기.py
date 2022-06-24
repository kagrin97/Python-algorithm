def solution(arr):
    answer = 0

    for i in range(len(arr)):
        answer += arr[i]
    answer = answer / len(arr)
    
    if answer % 1 == 0:
        return int(answer)
    return answer


n = [5, 5]
print(solution(n))




