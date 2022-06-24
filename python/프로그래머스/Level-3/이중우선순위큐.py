import heapq
def solution(operations):
    new_op = []
    heap = []

    for i in operations:
        new_op.append(i.split()) # [['I', '16'], ['D', '1']] 변환

    for i in range(len(new_op)):
        if new_op[i][0] == 'I':
            heapq.heappush(heap, int(new_op[i][1])) # 문자열을 정수로 바꿔넣음
        elif new_op[i][0] == 'D':
            if new_op[i][1] == '-1': 
                try:
                    heapq.heappop(heap) # 최소값 제거
                except:
                    pass
            else:
                try:
                    heap.remove(max(heap)) # 최대값 제거
                except:
                    pass
                
    if heap: 
        return [max(heap), min(heap)]
    else: # 비어 있으면 0, 0 출력
        return [0, 0]
        
operations = ["I 16","D 1"]
print(solution(operations))


