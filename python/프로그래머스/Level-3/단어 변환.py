count = 0
def dfs(begin, target, words, visited):
    global count 
    stack = [begin]

    while stack:
        alpha = stack.pop()

        if alpha == target:
            return count

        for i in range(len(words)):
            if len([j for j in range(len(words[i])) if words[i][j] != alpha[j]]) == 1:
                if visited[i] != 0:
                    continue
                visited[i] = 1
                stack.append(words[i])
        count += 1

def solution(begin, target, words):
    global count

    if target not in words:
        return 0

    visited = [0 for i in range(len(words))]
    dfs(begin, target, words, visited)
    return count


begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))

'''
13번째줄은 모든 문자열을 비교해 하나만 틀렸다면 실행되는 조건문이다 
'''