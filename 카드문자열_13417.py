answer = []
T = int(input())
for _ in range(T):
    tmp = []
    N = int(input())
    card = list(input().split())
    for i in range(len(card)):
        if i == 0:
            tmp.append(card[0])
        else:
            if tmp[0] < card[i]:
                tmp.append(card[i])
            else:
                tmp.insert(0,card[i])
    answer.append("".join(tmp))
for i in answer:
    print(i)





