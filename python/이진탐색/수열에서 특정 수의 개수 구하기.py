'''
오름차순 정렬된 수열에서 특정 수의 개수 구하기
'''


from bisect import bisect_left, bisect_right
# 특정수의 제일 왼쪽 인덱스와 오른쪽 인덱스를 구하기위한 모듈


def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    # 제일 오른쪽 인덱스를 구함
    left_index = bisect_left(array, left_value)
    # 제일 왼쪽 인덱스를 구함
    return right_index - left_value
    # 둘이 빼면 총 길이가 나옴 그 수를 리턴


n, x = map(int, input().split())
# 수열의 길이 x 원하는 특정수 x
array = list(map(int, input().split()))
# 수열을 입력 받음 (오름차순)
count = count_by_range(array, x, x)
# 함수를 실행하고 값을 count에 저장

if count == 0:
    print(-1)
    # 값이 없을경우 -1을 출력
else:
    print(count)
