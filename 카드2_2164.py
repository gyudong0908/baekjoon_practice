# 홀수와 짝수일때를 구분지어 버리는 카드 없애기
n = int(input())
card = list(range(1,n+1))

if len(card) == 1:
    print(1)
else:
    i = len(card) % 2
    while len(card) > 1:
        if i==0:
            card = card[1::2]
            i = len(card) % 2
        else:
            card = [card[-1], *card[1::2]] # 홀수일때는 무조건 0번 index부터 카드가 사라지도록
            i = len(card) % 2              # card의 마지막 index를 앞에 추가
    print(int(card[0]))

# queue를 사용하여 문제 해결
# from collections import deque
# n = int(input())
# card = deque(list(range(1,n+1)))
# while len(card) > 1:
#     card.popleft()
#     card.append(card.popleft())
# print(card[0])
