# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))
#
# data.sort()
# f = data[n - 1]
# s = data[n - 2]
# result = 0
#
# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += f
#         m -= 1
#
#     if m == 0:
#         break
#
#     result += s
#     m -= 1
#
# print(result)

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
f = data[n - 1]
s = data[n - 2]

count = k * int(m / (k + 1))
count += m % (k + 1)
result = 0

result += (f * count) + ((m - count) * s)

print(result)