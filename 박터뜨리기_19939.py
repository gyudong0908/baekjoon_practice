# N개의 공을 K개의 바구니에 빠짐없이 나누어 담는다.
# 각 바구니에는 1개 이상의 공이 들어 있어야 한다.
# 각 바구니에 담긴 공의 개수는 모두 달라야 한다.
# 가장 많이 담긴 바구니와 가장 적게 담긴 바구니의 공의 개수 차이가 최소가 되어야 한다.
N,K = map(int,input().split())
result = K-1
if N < sum(range(K+1)):
    print(-1)
else:
    N -= sum(range(K+1))
    if N % K == 0:
        print(result)
    else:
        print(result+1)
