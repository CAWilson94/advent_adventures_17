from itertools import cycle
from december_03 import moves as m


def generate_spiral(end_point, larger_val):
    n = 1
    pos = 0, 0
    times_to_move = 1
    moves_boop = [m.move_right, m.move_up, m.move_left, m.move_down]

    _moves = cycle(moves_boop)
    yield n, pos

    neighbours = {pos: n}

    while True:
        for item in range(2):  # Go through moves list twice to get whole spiral..until cut off at return
            move = next(_moves)
            for items in range(times_to_move):
                if n >= end_point:
                    print("The larger value is: " + str(find_larger_value(neighbours, larger_val)))
                    return
                pos = move(*pos)  # Argument unpacking woo
                n = get_neighbours_sum(pos, neighbours)
                neighbours[pos] = n
                yield n, pos
        times_to_move += 1


def get_num_moves_largest(end_point, larger_val):
    spiral = list(generate_spiral(end_point, larger_val))
    steps = spiral[len(spiral) - 1][1]
    total_steps = abs(steps[0]) + abs(steps[1])
    return total_steps


def get_neighbours_sum(current_pos, current_neighbours):
    other_items = [m.move_right, m.move_right_diagonal_up, m.move_up, m.move_left_diagonal_up,
                   m.move_left, m.move_right_diagonal_down, m.move_down, m.move_left_diagonal_down]
    sum_list = []

    for item in range(len(other_items)):
        pos_new = other_items[item](*current_pos)
        if pos_new in current_neighbours:
            sum_list.append(current_neighbours[pos_new])
    return sum(sum_list)


def find_larger_value(values_dict, value_to_find):
    for value in values_dict.values():
        if value > value_to_find:
            return value


if __name__ == "__main__":
    get_num_moves_largest(277678, 277678)





