from collections import defaultdict


num_cities = int(input())
matrix = []
for _ in range(num_cities):
    row = list(map(int, input().split()))
    matrix.append(row)

adj_list = defaultdict(list)
for i in range(num_cities):
    for j in range(num_cities):
        if matrix[i][j] == 1:
            adj_list[i].append(j+1)

for i in range(num_cities):
    print(len(adj_list[i]), *adj_list[i])