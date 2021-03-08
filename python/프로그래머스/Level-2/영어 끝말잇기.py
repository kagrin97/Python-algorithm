def solution(n, words):
    ans = [0, 0]

    for i in range(1, len(words)): # 비교를위한 0번째를 제외한 모두 검사
        if words[i-1][-1] != words[i][0] or words[i] in words[:i]: # 끝말잇기 룰이 성립하지 않을떄
            ans[0] = (i % n) + 1 # 몇번째로 돌아온건지
            ans[1] = (i // n) + 1 # 몇번째 차례인지
            break
    return ans

n = 3
w = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution(n, w))

'''
끝말잇기를 n명이서 하는데 도중에 끝말잇기를 못한 사람이 몇번 대답했는지
건지와 n명중 순서는어떻게 되는지를 물어보는 문제

어째서 (i%n) +1 이 차례인지를 이해는 안되지만 계산해보니 맞다 ;;
'''