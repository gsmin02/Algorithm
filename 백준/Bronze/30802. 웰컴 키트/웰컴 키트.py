num = int(input())
order = list(map(int, input().split()))
T, P = map(int, input().split())
T_sets = 0

for i in order:
    if i == 0:
        continue
    elif i <= T:
        T_sets += 1
    elif i % T == 0:
        T_sets += (i // T)
    else:
        T_sets += (i // T) +1

P_sets = num // P
res = num % P

print(T_sets)
print(f"{P_sets} {res}")