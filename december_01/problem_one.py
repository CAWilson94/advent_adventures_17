def non_human_captcha(puzzle_input):
    sum_array = []
    for x in range(len(puzzle_input)):
        next_val = puzzle_input[(x + 1) % len(puzzle_input)]
        if puzzle_input[x] == next_val:
            sum_array.append(puzzle_input[x])
    return sum(sum_array)
