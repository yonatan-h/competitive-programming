def main():
    num_ppl_in_family = int(input())
    rooms = input().split()

    unique_rooms = set()
    repeated_rooms = set()

    for room in rooms:
        in_unique = room in unique_rooms
        in_repeated = room in repeated_rooms

        if in_repeated:
            pass
        elif in_unique:
            unique_rooms.remove(room)
            repeated_rooms.add(room)
        else:
            unique_rooms.add(room)
    
    for room in unique_rooms:
        print(room)

main()

#20min
#1sub