'''
단어 정렬
'''

xy = list(set([input() for _ in range(int(input()))]))
# 입력받는 횟수를 위해 range를 썻고 그값을 set로 받은다음 list형태로 저장한다
xy.sort(key=lambda x: (len(x), x))
# 람다식을 이용해 길이순서로 정렬하고 길이가 같으면 사전순으로 정렬을함
print("\n".join(xy))
# join을 이용해 값들을 합쳐주고 \n을 이용해 한줄씩 출력한다
