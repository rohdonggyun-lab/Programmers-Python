def solution(num_list):
    answer = 0
    a=1
    b=0
    for i in num_list:
        a*=i
    for j in num_list:
        b+=j
    k=b**2
    if a<k:
        answer = 1
    else:
        answer = 0
    return answer