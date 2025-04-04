N, M = map(int, input().split())

matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))

sum_matrix = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(N):
    for j in range(N):
        sum_matrix[i + 1][j + 1] = (matrix[i][j] + sum_matrix[i + 1][j] + sum_matrix[i][j + 1] - sum_matrix[i][j])

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = (sum_matrix[x2][y2] - sum_matrix[x1 - 1][y2] - sum_matrix[x2][y1 - 1] + sum_matrix[x1 - 1][y1 - 1])
    print(result)