def solution(citations):
    citations.sort()
    
    s = len(citations)
    for i in range(s):
        if citations[i] >= s - i:
            return s - i
    return 0


phone_book = [3, 0, 6, 1, 5]
print(solution(phone_book))
