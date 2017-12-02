def non_human_captcha_2(puzzle_input):
    length_puzzle_input = len(puzzle_input) * 2
    comp_val = int(len(puzzle_input) / 2)
    sum_array = []

    for x in range(int(length_puzzle_input/2)):
        current_val = puzzle_input[x % len(puzzle_input)]
        next_val = puzzle_input[(x+comp_val) % len(puzzle_input)]
        if current_val == next_val:
            sum_array.append(current_val)
    return sum(sum_array)
