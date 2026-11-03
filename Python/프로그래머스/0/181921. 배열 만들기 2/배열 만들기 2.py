def solution(l, r):
    answer = []
    for i in range(1, 64):
        num = int(bin(i)[2:]) * 5   # 이진수 문자열을 십진수로 읽고 5를 곱함
        if l <= num <= r:
            answer.append(num)
    return answer if answer else [-1]