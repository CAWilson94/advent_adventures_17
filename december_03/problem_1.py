from itertools import cycle


def _move_right(x, y):
    """ Move right on the grid """
    return x+1, y


def _move_left(x, y):
    """ Move left on the grid """
    return x-1, y


def _move_up(x, y):
    """ Move up on the grid """
    return x, y + 1


def _move_down(x, y):
    """ Move down on the grid """
    return x, y-1


def _generate_spiral(end_point):
    n = 1
    pos = 0, 0
    times_to_move = 1
    moves_boop = [_move_right, _move_up, _move_left, _move_down]

    _moves = cycle(moves_boop)
    yield n, pos

    while True:
        for item in range(2):  # Go through moves list twice to get whole spiral..until cut off at return
            move = next(_moves)
            for items in range(times_to_move):
                if n >= end_point:
                    return
                pos = move(*pos)  # Argument unpacking woo
                n += 1
                yield n, pos
        times_to_move += 1


def get_num_moves(end_point):
    la = list(_generate_spiral(end_point))
    steps = la[len(la) - 1][1]
    total_steps = abs(steps[0]) + abs(steps[1])
    return total_steps

