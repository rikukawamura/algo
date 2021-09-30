import pdb
import queue

def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

N, M = int_sp()
rel = [[] for _ in range(N)]
for _ in range(M):
    A, B = int_sp()
    rel[A].append(B)
    rel[B].append(A)
q = queue.Queue()
p = queue.Queue()
visited = [False]*N # 各頂点を訪れたかを記録
visited[0] = True
q.put(0)
print(0)
for i in range(N-1):
    while not p.empty():
        q.put(p.get())
    while not q.empty():
        x = q.get()
        for i in rel[x]:
            if visited[i] != True:
                visited[i] = True
                p.put(i)
        if all(visited):
            print(*sorted(vars(p)['queue']))
            exit()
    print(*sorted(vars(p)['queue']))





