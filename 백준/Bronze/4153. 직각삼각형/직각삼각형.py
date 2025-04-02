while True:
    num = list(map(int, input().split()))
    if sum(num) == 0:
        break
    val = max(num)
    num.remove(val)
    if num[0]**2 + num[1]**2 == val**2:
        print('right')
    else:
        print('wrong')