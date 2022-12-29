# 입력값 받기
N = int(input())
l = list(map(int,input().split()))
atack = sorted( l[1:])
answer = 'Yes'

for i in atack:
    if l[0] > i:
        l[0] += i
    elif l[0] <= i:
        answer = 'No'
        break
print(answer)
