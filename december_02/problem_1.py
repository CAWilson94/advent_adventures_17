def check_sum_1(puzzle_input):
    """ For each row, determine the difference between
        the largest value and the smallest value;
        the checksum is the sum of all of these differences.
    """
    difference = []
    for index, row in puzzle_input.iterrows():
        difference.append(max(row) - min(row))
    return sum(difference)
