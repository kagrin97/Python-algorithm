for tc in range(int(input())):
    # 테스트 케이스 입력
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])
        index += m
    # 인덱스 슬라이싱으로 2차원 배열을 만듦
    for j in range(1, m):
        # 맨 왼쪽열은 이미 값이 부여되 있기때문에 1부터 시작
        for i in range(n):
            if i == 0:
                left_up = 0
            # 현재 위치가 제일 위라서 왼쪽위 값을 더할수 없기 때문에 0을 부여
            else:
                left_up = dp[i - 1][j - 1]
            # 현재 위치가 제일 위가 아니라면 왼쪽위 값을 넣어라
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            left = dp[i][j - 1]
            # 왼쪽값
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
            # 현재 인덱스값과 왼위,왼아래,왼 중에 가장 큰값을 더해줌
    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])
        # 맨 오른쪽 끝에있는 값 중에 가장 큰값을 저장
    print(result)

            

            

