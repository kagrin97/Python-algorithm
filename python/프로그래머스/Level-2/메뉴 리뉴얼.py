from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []

    for kind in course: # 2,3,4 종류마다
        k_list = [] # 임시 리스트
        for menu in orders:
            for i in combinations(menu, kind): # 메뉴마다 k만큼의 종류 조합
                k_list.append(''.join(sorted((i)))) # AC, CA 를 막기위한 정렬과 합쳐서 넣어줌
        k_counter = Counter(k_list).most_common() # 카운터로 딕셔너리 형태로 저장
        print(k_counter) 
        answer += [menu for menu, cnt in k_counter if cnt > 1 and cnt == k_counter[0][1]]
        # k_counter에서 Menu, cnt를 꺼내서 만약 cnt가 2이상 최대 주문 횟수일때만 menu를 저장
    return sorted(answer)

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
print(solution(orders, course))

'''
이 문제는 Counter(k_list).most_common() 를 사용해서 [('CDE', 3), ('BCF', 2), ('BCG', 2)]
와 같이 조합과 함께 그 조합이 몇개인지 세준다 (딕셔너리 형태로)
카운터는 자동으로 주문횟수의 내림차순으로 정렬을 해준다
cnt == k_counter[0][1]의 존재 이유는 문제에 최대 주문 횟수 만 추가 즉 2가지로 이뤄진 메뉴중
가장 많은 횟수를 시킨 메뉴만 추가한다 주문횟수가 큰 값이 여러개 일경우를 위한 cnt ==
가 있따
'''