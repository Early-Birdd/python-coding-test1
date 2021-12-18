# 구현 2번

data = input()
row = int(data[1])
# ord -> 아스키코드 (0~9 : 48~57) (A~Z : 65~90) (a~z : 97~122)
column = int(ord(data[0])) - int(ord('a')) + 1

go_data = [(-1, -2), (-1, 2), (1, 2), (1, -2), (-2, -1), (-2, 1), (2, -1), (2, 1)]
count = 0

for i in go_data:
    nr = row + i[0]
    nc = column + i[1]
    if nr <= 1 or nc <= 1 or nr >= 8 or nc >= 8:
        continue
    count += 1

print(count)