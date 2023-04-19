num_cities = int(input())
num_roads = 0
for _ in range(num_cities):
    row = list(map(int, input().split()))
    num_roads += sum(row)

print(num_roads//2)