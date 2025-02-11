def recursive(n):
    if n == 1:
        return ['*']
    
    a = recursive(n // 3)
    
    L = (
        [b * 3 for b in a] +
        [b + ' ' * (n // 3) + b for b in a] +
        [b * 3 for b in a]
    )
    
    return L

N = int(input())
result = recursive(N)

for str in result:
    print(str)