def recursive(n, s, e):
    if n == 1:
        print(s, e)
        return
    
    num = 6 - s - e
    recursive(n-1, s, num)
    print(s, e)
    recursive(n-1, num, e)

N = int(input())
print(2**N - 1)
recursive(N, 1, 3)