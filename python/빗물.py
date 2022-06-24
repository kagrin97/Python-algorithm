H, W = map(int, input().split())
rain = list(map(int, input().split()))
water = 0
for i in range(len(rain)):
    max_left = max(rain[:i+1]) # 현재 인덱스의 왼쪽에서 가장 높은 건물의 높이를 구한다
    max_right = max(rain[i:]) # 현재 인덱스의 오른쪽에서 가장 높은 건물의 높이를 구한다
    which_min = min(max_left, max_right) # 그중 더 낮은 건물의 높이를 구한다
    water = water + (which_min - rain[i]) # 그 높이에서 현재 인덱스에 있는 건물의 높이를 뺀다
print(water)

'''
이 문제는 쉽게 푸는 알고리즘이 있는데
현재 인덱스의 왼쪽, 오른쪽 각각 가장 높은 건물을 구한다음(자신의높이 포함)
둘중 더작은 건물의 높이 - 현재 인덱스높이 = 고이는 빗물의 양이라는 
놀라운 풀이 방법이있따
'''