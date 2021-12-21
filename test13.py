#정렬 2번

n = int(input())

data = []
for i in range(n):
    data.append(int(input()))
    
data = sorted(data, reverse = True)
print(data)