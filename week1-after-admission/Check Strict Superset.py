def is_superset(superset, numbers):
    for number in numbers:
        if number not in superset:
            return False
    return True


def main():
    super_set_numbers = [int(string_num) for string_num in input().split()]
    super_set = set(super_set_numbers)
    
    other_sets = int(input())

    for i in range(other_sets):
        numbers = [int(string_num) for string_num in input().split()]
        
        if (len(numbers) > len(super_set_numbers)):
           return False
        
        if not is_superset(super_set, numbers):
            return False
        
    return True

print(main())

#1:30