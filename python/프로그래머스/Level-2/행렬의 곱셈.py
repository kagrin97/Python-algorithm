def solution(arr1, arr2):
    answer = []
    for idx1 in range(len(arr1)):
        row = []
        for idx2 in range(len(arr2[0])):
            tmp = 0
            for idx3 in range(len(arr1[0])):
                tmp += arr1[idx1][idx3] * arr2[idx3][idx2]
            row.append(tmp)
        answer.append(row)
    return answer

a = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
b = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]

print(solution(a, b))

