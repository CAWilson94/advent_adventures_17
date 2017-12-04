def split_strings_to_list(puzzle_input):
    input_list = []
    for item in puzzle_input:
        input_list.append(split_string_to_list(item.upper()))
    return input_list


def split_string_to_list(some_string):
    content = some_string.split()
    return content


def problem_1(puzzle_input):
    """ problem description """
    valid_phrase = 0
    for item in puzzle_input:
        sets = set([x for x in item if item.count(x) > 1])
        if sets == set():
            valid_phrase += 1
    return valid_phrase



