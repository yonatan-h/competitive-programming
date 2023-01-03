class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        return find_nearest_point(x,y,points)

def find_nearest_point(x_center, y_center, points):
    index_of_nearest = -1
    smallest_manhattan_distance = float('inf')

    for i in range(len(points)):
        point = points[i]
        x_point = point[0]
        y_point = point[1]
        manhattan_distance = abs(x_center - x_point) + abs(y_center - y_point)

        is_valid = x_center == x_point or y_center == y_point
        is_closest = manhattan_distance < smallest_manhattan_distance

        if is_valid and is_closest:
            index_of_nearest = i
            smallest_manhattan_distance = manhattan_distance

    return index_of_nearest
