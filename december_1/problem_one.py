def non_human_captcha(puzzle_input):
    """ Non Human Captcha Puzzle """
    sum_array = []
    for index in range(len(puzzle_input)-1):
        if puzzle_input[index + 1] == puzzle_input[index]:
            sum_array.append(puzzle_input[index])
    if puzzle_input[0] == puzzle_input[-1]: # Such a hack ...
        sum_array.append(puzzle_input[0])
    captcha_answer = sum(sum_array)
    return captcha_answer

