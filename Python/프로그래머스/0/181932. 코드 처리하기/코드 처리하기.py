def solution(code):
    mode = 0
    ret = []
    for idx, c in enumerate(code):
        if c == "1":
            mode ^= 1              # 0 ↔ 1 토글
        elif idx % 2 == mode:      # mode 0이면 짝수, mode 1이면 홀수 인덱스
            ret.append(c)
    return "".join(ret) or "EMPTY"