A, B = map(int, input().split())
q = [(B, 1)]
result = -1
while q:
    x, cnt = q.pop(0)
    if x == A:
        result = cnt
        break

    if x % 2 == 0 and x / 2 >= A:
        q.append((x / 2, cnt + 1))
    elif x % 10 == 1 and x / 10 >= A:
        q.append((x // 10, cnt + 1))
    else:
        break

print(result)

'''
정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.

2를 곱한다.
1을 수의 가장 오른쪽에 추가한다. 
A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

BFS로 푸는 문제이다 먼저 B가 2로 나누어지고 나눠도 A보다 클경우 2로 나눠준다
2로 나눠지지 않고 B의 1의자리가 1이고 1을 빼도 A보다 클경우 1을 빼준다
둘다 해당하지 않을 경우 -1을 출력한다
'''