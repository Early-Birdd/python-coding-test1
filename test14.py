#정렬 3번

n = int(input())

data = []
for i in range(n):
    put_data = input().split()
    #append((a,b))
    data.append((put_data[0], int(put_data[1])))

data = sorted(data, key = lambda student : student[1])

for i in data:
    print(i[0], end = ' ')