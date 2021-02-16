def solution(strings, n):

    answer = sorted(sorted(strings), key = lambda x : x[n])
    # 람다로 n번째 순으로 정렬을 하였다 sorted를 2번한 이유는 n인덱스
    #  문자가 여럿일 경우 사전순 정렬을 위해서 였다
    return answer

s = ["abce", "abcd", "cdx"]
n = 2
print(solution(s, n))

'''
문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 
각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다. 
예를 들어 strings가 [sun, bed, car]이고 
n이 1이면 각 단어의 인덱스 1의 문자 u, e, a로 strings를 정렬합니다.
인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치합니다.
마지막 조건 때문에 삽질 하다가 풀어내었다
'''