def solution(a, b):
    answer = 0
    l=str(a)+str(b)
    r=str(b)+str(a)
    if int(l) >= int(r) :
        return int(l)
    else:
        return int(r)
