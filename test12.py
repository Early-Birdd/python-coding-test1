#정렬 1-선택 정렬

# data = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
#
# for i in range(len(data)):
#     for j in range(i + 1, len(data)):
#         if data[i] > data[j]:
#             data[i], data[j] = data[j], data[i]
#
# print(data)

#정렬 1-삽입 정렬

# data = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
#
# for i in range(1, len(data)):
#     #i부터 1까지 1씩 감소하며
#     for j in range(i, 0, -1):
#         if data[j] < data[j - 1]:
#             data[j], data[j - 1] = data[j - 1], data[j]
#         else:
#             break
#
# print(data)

#정렬 1-퀵 정렬

# data = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
#
# def q_sort(data, start, end):
#     if start >= end:
#         return
#
#     pivot = start
#     left = start + 1
#     right = end
#     while left <= right:
#         while left <= end and data[left] <= data[pivot]:
#             left += 1
#         while right > start and data[right] >= data[pivot]:
#             right -= 1
#         if left > right:
#             data[pivot], data[right] = data[right], data[pivot]
#         else:
#             data[left], data[right] = data[right], data[left]
#     q_sort(data, start, right - 1)
#     q_sort(data, right + 1, end)
#
# q_sort(data, 0, len(data) - 1)
# print(data)

#정렬 1-퀵 정렬(2)

# data = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
#
# def q_sort(data):
#     if len(data) <= 1:
#         return data
#
#     pivot = data[0]
#     tail = data[1:]
#
#     left = [x for x in tail if x < pivot]
#     right = [x for x in tail if x > pivot]
#
#     return q_sort(left) + [pivot] + q_sort(right)
#
# print(q_sort(data))

#정렬 1-계수 정렬

# data = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
#
# count = [0] * (max(data) + 1)
#
# for i in range(len(data)):
#     count[data[i]] += 1
#
# for j in range(len(data)):
#     for k in range(count[j]):
#         print(j, end = ' ')

#정렬 1-python sorted

# data = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
#
# result = sorted(data)
# print(result)

#정렬 1-python sort

# data = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
#
# data.sort()
# print(data)

#정렬 1-python sort

data = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(array):
    return array[1]

result = sorted(data, key = setting)
print(result)