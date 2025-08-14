import sys
input = sys.stdin.readline

N = int(input())
arrN = list(map(int, input().split()))
M = int(input())
arrM = list(map(int, input().split()))

arrN = sorted(arrN)
for m in arrM:
    chk = False
    start, end = 0, N - 1
    while start <= end:
        mid = (start + end) // 2
        if m == arrN[mid]:
            chk = True
            break
        elif m > arrN[mid]:
            start = mid + 1
        else:
            end = mid - 1
    if chk:
        print("1")
    else:
        print("0")