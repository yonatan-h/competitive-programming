def can_form_triangle(side1, side2, side3):
    longest_side = max(side1 + side2 + side3)
    perimeter = side1 + side2 + side3

    if longest_side >= perimeter/2:
        return False
    elif perimeter == 0:
        return False
    else:
        return True

def find_longest_triangle(sides):
    longest_perimeter = 0

    for i in range(len(sides)-3):
        current_perimeter = sides[i] + sides[i+1] + sides[i+2]
        if can_form_triangle(sides[i], sides[i+1], sides[i+2]):
            longest_perimeter = max(longest_perimeter, current_perimeter)
    
    return longest_perimeter



#15min
#2sub
