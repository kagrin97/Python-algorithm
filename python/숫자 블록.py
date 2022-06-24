import math

def solution(begin, end):
    answer = []

    for i in range(begin, end + 1):
        if i == 1:
            answer.append(0)
        else:
            sqrt = int(math.sqrt(i))
            for j in range(2, sqrt + 1):
                mok = i // j
                if mok > 10 ** 7: # 길의 길이가 블록보다 길어서 짤라줘야함
                    continue
                elif i % j == 0: # 가장 먼저 짤리는 수의 몫이 가장큰 약수임
                    answer.append(mok)
                    break
            else: # for-else는 for문에서 break로 나오면 실행이 안됨
                answer.append(1)  # 소수라서 1

    return answer
begin = 1
end = 10
print(solution(begin, end))