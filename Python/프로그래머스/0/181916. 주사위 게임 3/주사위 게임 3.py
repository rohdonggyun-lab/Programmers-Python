from collections import Counter

def solution(a, b, c, d):
    cnt = Counter([a, b, c, d]).most_common()  # (숫자, 개수)를 개수 많은 순으로 정렬

    if len(cnt) == 1:                     # 모두 같음
        p = cnt[0][0]
        return 1111 * p
    if len(cnt) == 2:
        (p, pc), (q, qc) = cnt
        if pc == 3:                       # 3개 + 1개
            return (10 * p + q) ** 2
        return (p + q) * abs(p - q)       # 2개 + 2개
    if len(cnt) == 3:                     # 2개 + 1개 + 1개
        q, r = cnt[1][0], cnt[2][0]
        return q * r
    return min(a, b, c, d)                # 모두 다름