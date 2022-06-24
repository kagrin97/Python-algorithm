n=int(input())
words=[]

for i in range(n):
  words.append(input())

dict={}
for word in words:
  k=len(word)-1 # 해당 문자의 최대 길이
  for s in word:
    if s in dict: # 문자 s가 사전에 있다면
      dict[s] += pow(10,k) # 해당 키에 자릿수에 맞는 값을 더 추가해줌
    else:
      dict[s] = pow(10,k) # 새로 생성
    k -= 1

nums=[]

for val in dict.values():
  nums.append(val) # 값들만 뽑아서 큰순으로 정렬

nums.sort(reverse=True)
result,t=0,9 

for i in range(len(nums)):
  result += nums[i] * t # 해당 숫자들에 9부터 1까지 큰순으로 곱해줌
  t -= 1

print(result)

'''
이 문제는 설명하기 어렵다 
'''