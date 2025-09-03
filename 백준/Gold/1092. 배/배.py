import sys

input = sys.stdin.readline

N = int(input())
arrN = list(map(int, input().split()))
M = int(input())
arrM = list(map(int, input().split()))

arrN.sort(reverse=True)
arrM.sort(reverse=True)

answer = 0
if arrM[0] > arrN[0]:
    answer = -1
else:
    time = 0
    while arrM:
        time += 1
        i = 0
        j = 0
        while i < N and j < len(arrM):
            if arrN[i] >= arrM[j]:
                arrM.pop(j)
                i += 1
            else:
                j += 1
    answer = time
print(answer)