num = int(input())

arr = []

for _ in range(num):
    start, end = map(int, input().split(" "))
    arr.append((start, end))

arr.sort(key=lambda x: (x[1], x[0]))

time = 0
result = 0
for meeting in arr:
    if time <= meeting[0]:
        time = meeting[1]
        result += 1

print(result)