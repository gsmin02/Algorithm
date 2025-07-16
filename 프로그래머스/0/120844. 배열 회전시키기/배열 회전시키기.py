def solution(numbers, direction):
    if direction == "right":
        tmp = numbers.pop()
        numbers.insert(0, tmp)
    elif direction == "left":
        tmp = numbers.pop(0)
        numbers.append(tmp)
    return numbers