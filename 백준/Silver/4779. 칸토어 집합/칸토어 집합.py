def div(m, n):
    if n < 1:
        return
    result[m + n // 3 : m + (n // 3) * 2] = [' '] * (n // 3)
    div(m, n // 3)
    div(m + (n // 3) * 2, n // 3)

while True:
    try:
        N = int(input())
        num = 3 ** N
        result = ['-'] * num
        div(0, num)
        
        for c in result:
            print(c, end='')
        print()
    except:
        break