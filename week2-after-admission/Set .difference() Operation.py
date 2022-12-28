# Enter your code here. Read input from STDIN. Print output to STDOUT
def main():
    english_nums = int(input())
    english_students = set(input().split(" "))

    french_nums = int(input())
    french_students = set(input().split(" "))

    only_english_students = english_students - french_students
    
    print(len(only_english_students))

main()

#6min
#1sub