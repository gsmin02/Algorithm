import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = list(list(map(int, input().split())) for _ in range(N))

x, y = 0, 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            x, y = i, j
            graph[i][j] = 0
            break

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
size = 2
def bfs(x, y):
    # 재탐색 판단
    visited = [[-1] * N for _ in range(N)]
    queue = deque([(x, y)])
    visited[x][y] = 0
    # 먹이 목록
    eating = []
    
    while queue:
        # 시작 위치
        n, m = queue.popleft()
        # 상하좌우 탐색
        for i in range(4):
            nx, ny = n + dx[i], m + dy[i]
            
            # N×N 크기
            if 0 <= nx < N and 0 <= ny < N:
                # 이동 가능 and 안 가본 곳
                if size >= graph[nx][ny] and visited[nx][ny] == -1:
                    # 이동 거리
                    visited[nx][ny] = visited[n][m] + 1
                    # 다음 갈 곳
                    queue.append((nx, ny))
                    # 먹을 수 있다면
                    if 0 < graph[nx][ny] < size:
                        # 먹이 목록에 추가
                        eating.append((visited[nx][ny], nx, ny))
    # 최적 먹이 반환
    return sorted(eating)

# 최소 시간
answer = 0
# 단계별 먹은 먹이
ate = 0
while True:
    # 먹이 탐색
    eat = deque(bfs(x, y))
    # 먹이 없는 경우 종료
    if not eat:
        break
    # 먹이 정보
    dist, nx, ny = eat.popleft()
    # 이동 거리
    answer += dist
    # size 대비 먹은 먹이
    ate += 1
    # 성장 조건 비교
    if size == ate:
        size += 1
        ate = 0
    # 시작 위치 먹이 위치로 변경
    graph[nx][ny] = 0
    x, y = nx, ny
# 최소 시간 출력
print(answer)