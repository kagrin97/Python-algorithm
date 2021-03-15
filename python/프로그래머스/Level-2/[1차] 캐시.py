def solution(cacheSize, cities):
    answer = 0
    cache = [] 
    low_cities = [] 
    if cacheSize == 0:
        return len(cities) * 5

    for i in cities:
        low_cities.append(i.lower())
    # 카카오 문제는 대문자 소문자가 섞여있어 구분하기위해 소문자로 바꿔준다
    for c in low_cities:
        if not c in cache: # 캐시에 없고
            if len(cache) < cacheSize: # 크기를 넘지 않으면
                cache.append(c) # 캐시에 넣고
                answer += 5 # 실행 시간이 크다
            else:
                cache.pop(0) # 캐시가 넘치면 빼고 넣는다
                cache.append(c) 
                answer += 5
        else:
            cache.pop(cache.index(c))
            cache.append(c)
            answer += 1
        # 캐시가 존재하면 해당 캐시를 삭제하고 넣고 존재하는것을 불러오기
        # 때문에 실행시간이 더 짧다
    return answer
        
                

cacheSize = 0
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(solution(cacheSize,cities))

'''
LRC 알고리즘은 한번쓴 데이터를 cacheSize가 넘치지 않으면
캐시에 저장 하고 cacheSize가 넘으면 제일 오래전에 넣은
데이터를 삭제하고 새로운 데이터를 캐시에 집어 넣는다
cache hit는 캐시에 데이터를 꺼내는 것으로 캐시안에 데이터가 존재해야함(속도가빠름)
cache miss는 캐시에 데이터가 없는 경우로 캐시에 저장하고 불러와야 하기때문에
속도가 cache hit보다 속도가 더 느리다
'''