def solution(a, b):
    answer = 0
    fx1=int(str(a) + str(b))
    fx2=2*a*b
    if fx1>fx2:
        answer=fx1
    else: 
        answer=fx2
    return answer