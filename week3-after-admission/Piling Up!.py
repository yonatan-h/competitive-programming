from collections import deque

def main():
    num_testcases = int(input())

    for _ in range(num_testcases):
        num_cubes = int(input())
        cubes = list(map(int, input().split()))
        if can_be_stacked(cubes):
            print("Yes")
        else:
            print("No")



def can_be_stacked(cubes):
    current_cubes = deque(cubes)
    top_stack_cube = float('inf')

    while current_cubes:
        left_cube = current_cubes[0]
        right_cube = current_cubes[-1]

        if max(left_cube, right_cube) > top_stack_cube:
            return False
        
        if right_cube > left_cube:
            top_stack_cube = right_cube
            current_cubes.pop()
        else:
            top_stack_cube = left_cube
            current_cubes.popleft()
    return True

main()

#15min
#1sub