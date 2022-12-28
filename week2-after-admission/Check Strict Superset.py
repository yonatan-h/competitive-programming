def main():
    super_set = set(input().split())

    num_following_sets = int(input())

    for i in range(num_following_sets):
        current_set = set(input().split())
        is_super_set = len(current_set - super_set) == 0
        is_strict_super_set = is_super_set and len(super_set) > len(current_set)
        
        if not is_strict_super_set:
            print(False)
            return

    print(True)

main()

#60min
#2sub