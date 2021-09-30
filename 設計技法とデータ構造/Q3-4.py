import pdb
import queue

def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

N, X = int_sp()
A = li_int_sp()
rel = [[] for _ in range(N)]
for to, fm in enumerate(A, 1):
    rel[fm].append(to)
#pdb.set_trace()
q = queue.Queue() # 現在の箱
p = queue.Queue() # 次の箱
q.put(0)
cnt = 1
#pdb.set_trace()
while True:
    # 次の箱の要素を現在の箱にうつす作業
    while not p.empty():
        q.put(p.get())
    # 各箱の中にXがあるかを探索
    while not q.empty():
        x = q.get()
        if X in rel[x]:
            print(cnt)
            exit()
        else:
            for i in rel[x]:
                p.put(i)

    # 現在の箱の要素にXがなければ箱の深さを+1する
    cnt += 1





