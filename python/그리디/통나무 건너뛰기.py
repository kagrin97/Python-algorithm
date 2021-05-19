T = int(input())

for _ in range(T):
    N = int(input())
    tree = list(map(int, input().split()))
    tree.sort()

    max_val = 0
    for i in range(2, N):
        max_val = max(max_val, abs(tree[i] - tree[i-2]))
    
    print(max_val)

'''
이문제는 해결 방법을 생각하지못해 인터넷의 힘을 빌렸다
기본 아이디어는 오름차순으로 정렬을 시키고
n개의 통나무가 있을 때 인접하는 통나무 사이의 최대 높이차는
 1번과 3번의 높이차, 2번과 4번의 높이차, ... n-2번과 n번의 높이차다.
  1번과 2번, n-1번과 n번도 인접하지만, 이것들은 각각 1번과 3번의 높이차, n-2번과 n번의 
높이차보다 작으므로 무시해도 좋다. 이를 바탕으로 아래의 코드를 완성했다.
'''