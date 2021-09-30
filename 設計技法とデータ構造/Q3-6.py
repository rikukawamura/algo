import pdb
import queue

def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

N = int(input())
A = li_int_sp()
rel = [[] for _ in range(N)]
for to, fm in enumerate(A, 1):
    rel[fm].append(to)
#pdb.set_trace()
q = queue.Queue() # 現在の箱
p = queue.Queue() # 次の箱
visited = [-1]*N
q.put(0)
cnt = 0
#pdb.set_trace()
for _ in range(N):
    # 次の箱の要素を現在の箱にうつす作業
    while not p.empty():
        q.put(p.get())
    # 各箱の中にXがあるかを探索
    while not q.empty():
        x = q.get()
        if visited[x] == -1:
            visited[x] = cnt
        for i in rel[x]:
            p.put(i)
    cnt += 1

for i in visited[1:]:
    print(i)





