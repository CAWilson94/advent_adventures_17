def check_sum_2(puzzle_input):
    """ find the only two numbers in each row where one evenly divides the other -
        that is, where the result of the division operation is a whole number.
        find those numbers on each line, divide them, and add up each line's result
    """
    difference = []
    for index, row in puzzle_input.iterrows():
        for item in range(len(row)):
            for other_item in range(item + 1, len(row)):
                if abs(row[item] % row[other_item]) == 0:
                    difference.append(row[item]/row[other_item])
                if abs(row[other_item] % row[item]) == 0:
                    difference.append(row[other_item] / row[item])
    return sum(difference)
