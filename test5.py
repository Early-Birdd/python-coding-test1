#구현 1-1

# n = int(input())
# go = input().split()
#
# x, y = 1, 1
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# data = ['L', 'R', 'U', 'D']
#
# for i in go:
#     for j in range(len(data)):
#         if i == data[j]:
#             # x += dx[j] 를 하면 범위를 벗어난 경우 x에 값이 저장된 상태로 진행되어 오답
#             nx = x + dx[j]
#             ny = y + dy[j]
#     if nx > n or ny > n or nx < 1 or ny < 1:
#         continue
#     # for문 밖에서 x, y값을 저장하면 2번째 for문 돌릴 때 x, y가 변하지 않고 1인 상태라서 오답
#     x = nx
#     y = ny
#
# print(x, y)

#구현 1-2

n = int(input())

count = 0

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)