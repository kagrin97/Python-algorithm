def solution(board, moves):
    answer = 0
    stack = [0] #index 에러를 막기위한 방법
    for i in moves:
        i -= 1 # 기본 moves 값이 0부터 시작이 아닌 1부터 시작이라서 1씩 빼준다
        for j in range(len(board)):
            if board[j][i] > 0: # 값이 있으면 뺴서 넣어주고 뺀공간을 비워준다
                stack.append(board[j][i])
                board[j][i] = 0
                if stack[-2] == stack[-1]: # 2수가 같으면 빼주고 정답에 +2
                    stack.pop()
                    stack.pop()
                    answer += 2
                break # 다음 moves값을 검사하기위한 break
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))