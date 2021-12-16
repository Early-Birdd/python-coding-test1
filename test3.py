# n, m = map(int, input().split())
#
# result = 0
#
# for i in range(n):
#     data = list(map(int, input().split()))
#     min_v = min(data)
#     result = max(result, min_v)
#
# print(result)

n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_v = 10001
    for j in data:
        min_v = min(min_v, j)
    result = max(result, min_v)

print(result)