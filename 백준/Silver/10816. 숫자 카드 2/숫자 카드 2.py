import sys

input = sys.stdin.readline

N = int(input())
arrN = list(map(int, input().split()))
M = int(input())
arrM = list(map(int, input().split()))

hashN = {}
for ele in arrN:
    hashN[ele] = hashN.get(ele, 0) + 1

ans = []
for n in arrM:
    ans.append(str(hashN.get(n, 0)))

print(" ".join(ans))