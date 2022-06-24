'''
떡볶이 떡 만들기 이.코.테
'''


n, m = list(map(int, input().split()))
# 떡의개수 n 필요한 떡의 길이 m
array = list(map(int, input().split()))
# 떡의 개별 길이가 주어짐
start = 0
end = max(array)
result = 0

while (start <= end):
    # 시작과 끝이 만날떄 까지
    total = 0
    mid = (start + end) // 2
    # 한번 돌릴떄 마다 초기화 시켜준다
    for x in array:
        if x > mid:
            # 떡의 길이가 중간 길이보다 길때만 떡을 얻을수 있어서
            total += x - mid
            # 자른 떡의 길이를 total에 저장
    if total < m:
        end = mid - 1
        # 자른 떡의 길이 총합이 원하는 값보다 적을경우 더 길게잘라야 하기위해
        # 왼쪽 탐색을 위해 end를 mid 왼쪽으로 설정
    else:
        result = mid
        start = mid + 1
        # 필요한 값을 얻었을경우 그 높이를 저장하고 더 좋은 높이를 찾기위해
        # 시작값을 mid 오른쪽에 배치해 조금더 높은 높이를 구함

print(result)
