# 입력 받기
N, M =  map(int, input().split())
P = []
max = [0,0]
for i in range(M):
    P.append(int(input()))

P.sort()
for idx, i in enumerate(P):
    if N > (len(P) - idx):
        cost = i * (len(P) - idx)
    else:
        cost = i * N
    if cost > max[1]:
        max[0] = i
        max[1] = cost
print(max[0], max[1])


