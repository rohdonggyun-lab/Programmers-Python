def solution(a, d, included):
    total, term = 0, a
    for inc in included:
        if inc:
            total += term
        term += d
    return total