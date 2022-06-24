'''
1. 0과 1로 만들어진 문자열이 있다
2. 이 문자열을 전부를 1이나 0으로 둘중 하나로 바꿔야 한다
3. 문자열이 주어 졌을떄 0으로 바꾸던지 1로 바꾸던지 전체를 다 바꿀수있는 최소횟수를 구해라
'''

s = input()

flag = False # 플래그 설정
count = 0
# 맨 앞의 숫자를 기준으로 두는게 최적이다.
head = s[0]

for x in s:
	# False인 경우 head와 현재 원소가 같으면 계산할 필요x, 달라질때 횟수 +1, True로 변경
    if flag == False:
        if x != head:
            flag = True
            count += 1
    # True인 경우 head와 현재 원소가 다르면 계산x, 헤드와 현재원소가 다르다가 똑같을때 False로 변경을해서 카운트 1을 추가
    else:
        if x == head:
            flag = False

print(count) # 헤드와 현재 원소가 달라질때마다 횟수를 증가시키고 true로 바꿔서 헤드와 같은 값이 나올때까지 돌린 다음에 같은값이나오면 다시 값을 증가시킨후 다시 돌림 