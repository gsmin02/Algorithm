import sys

input = sys.stdin.readline

n = int(input())
A, B, C, D = [], [], [], []

for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB = []
CD = []
for i in range(n):
    for j in range(n):
        AB.append(A[i] + B[j])
        CD.append(C[i] + D[j])

AB.sort()
CD.sort()

count = 0
left = 0
right = len(CD) - 1
while left < len(AB) and right >= 0:
    curr = AB[left] + CD[right]

    if curr == 0:
        count_ab = 0
        tmp_left = left
        while tmp_left < len(AB) and AB[tmp_left] == AB[left]:
            count_ab += 1
            tmp_left += 1

        count_cd = 0
        tmp_right = right
        while tmp_right >= 0 and CD[tmp_right] == CD[right]:
            count_cd += 1
            tmp_right -= 1
        
        count += (count_ab * count_cd)
        
        left = tmp_left
        right = tmp_right

    elif curr < 0:
        left += 1
    else:
        right -= 1

print(count)