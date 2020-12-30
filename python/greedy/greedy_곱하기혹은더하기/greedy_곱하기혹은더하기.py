'''
1. 0~9로 이루어진 문자열 s가 주어진다
2. 왼쪽부터 하나씩 숫자를 확인하면서 x,+ 를 이용해 가장 큰값을 구해라
'''

s = input()
result = int(s[0]) # 첫번째 값을 결과에 저장
 
for i in range(1, len(s)): # 숫자 길이만큼 반복
    num = int(s[i]) # 순서대로 인덱스 값을 int값으로 바꾸어 저장
    if result <= 1 or num <= 1: # 연산하는 두 숫자중 하나라도 1이하면 더하기
        result += num
    else: # 둘다 2이상 이라면 둘다 곱하기
        result *= num

print(result)