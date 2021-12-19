#DFS/BFS -> 자료구조 기초-1

# stack = []
#
# stack.append(5)
# stack.append(2)
# stack.append(3)
# stack.append(7)
# stack.pop()
# stack.append(1)
# stack.append(4)
# stack.pop()
#
# print(stack) #최하단 원소부터
# print(stack[::-1]) #최상단 원소부터

#DFS/BFS -> 자료구조 기초-2

# from collections import deque
#
# queue = deque()
#
# queue.append(5)
# queue.append(2)
# queue.append(3)
# queue.append(7)
# queue.popleft()
# queue.append(1)
# queue.append(4)
# queue.popleft()
#
# print(queue)
# queue.reverse()
# print(queue)

#DFS/BFS -> 자료구조 기초-3

# def recursive_function():
#     print('재귀')
#     recursive_function()
#
# recursive_function()

#DFS/BFS -> 자료구조 기초-4

# def recursive_function(i):
#     if i == 100:
#         return
#     print(i, '번째 재귀 함수에서', i + 1, '번째 재귀함수를 호출')
#     recursive_function(i+1)
#     print(i, '번째 재귀 종료')
#
# recursive_function(1)

#DFS/BFS -> 자료구조 기초-5

def fac_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def fac_recursive(n):
    if n < 1:
        return 1
    return n * fac_recursive(n - 1)

print('반복 구현 ', fac_iterative(5))
print('재귀 구현 ', fac_recursive(5))