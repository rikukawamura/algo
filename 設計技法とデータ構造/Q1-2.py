def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
N = int(input())
cnt = 0
tmp = 0
while N != 0:
    if N%2 == 1:
        N -= 1
        cnt += 1
    else:
        N //= 2
        cnt += 1

print(cnt)