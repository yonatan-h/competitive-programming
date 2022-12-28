# Enter your code here. Read input from STDIN. Print output to STDOUT
def main():
    english_nums = int(input())
    english_students = set(input().split(" "))

    french_nums = int(input())
    french_students = set(input().split(" "))

    all_students = english_students.union(french_students)
    
    print(len(all_students))

main()

#3min
#1sub