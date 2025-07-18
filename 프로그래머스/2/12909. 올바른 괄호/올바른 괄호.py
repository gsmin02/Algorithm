def solution(s):
    stack = []
    for c in s:
        if c in '(':
            stack.append(c)
        elif c in ')':
            if not stack or stack.pop() != '(':
                return False
    return True if len(stack) == 0 else False