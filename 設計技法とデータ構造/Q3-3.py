import pdb

def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

N, M, X = int_sp()
rel = [[] for _ in range(N)]
for _ in range(M):
    A, B = int_sp()
    rel[A].append(B)
    rel[B].append(A)
#pdb.set_trace()
cnt = 0
friends = rel[X]
friends_friends = set()
for i in friends: # アルルの友達
    for j in [x for x in rel[i] if x not in friends and x != X]:
        friends_friends.add(j)
print(len(friends_friends))
