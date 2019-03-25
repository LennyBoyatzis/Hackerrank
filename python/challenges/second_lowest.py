def second_lowest(students) -> int:
    lowest, second_lowest = float('inf'), float('inf')

    for student in students:
        if student[1] <= lowest:
            lowest, second_lowest = student[1], lowest
        elif student[1] < second_lowest:
            second_lowest = student[1]
    return second_lowest
