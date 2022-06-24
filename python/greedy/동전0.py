'''
누군가 k원을 주어서 민규는 거슬러 줘야한다
민규가 가지고 있는 동전은 n종류이고 동전을 적절히 사용해서 거슬러줄수있는 
동전 횟수의 최솟값을 구해야한다
'''

n, k = map(int, input().split())  # n = 동전의개수, k = 총 가격
array = []  # 이렇게해야지 에러가 안나온다
for i in range(n):  # 동전의 개수만큼 동전의 종류를 입력 받는다
    array.append(int(input()))
count = 0
array.sort(reverse=True)  # 내림차순의로 해서 최솟값을 구한다

for i in array:
    if k >= i:  # 총 가격보다 동전의 크기가 작을때만 작동한다
        count += k // i  # 나눈 횟수를 저장한다
        k %= i  # 총가격에 나눈값의 나머지를 저장해 위에부터 반복한다

print(count)
