def solution(n, control):
    answer = 0
    for ch in control:
        if ch == 'w':
            n += 1
        elif ch == 's':
            n -= 1
        elif ch == 'd':
            n += 10
        elif ch == 'a':
            n -= 10
    answer = n
    return answer