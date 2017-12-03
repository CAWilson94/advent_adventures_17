def move_right(x, y):
    """ Move right on the grid """
    return x + 1, y


def move_left(x, y):
    """ Move left on the grid """
    return x - 1, y


def move_up(x, y):
    """ Move up on the grid """
    return x, y + 1


def move_down(x, y):
    """ Move down on the grid """
    return x, y - 1


def move_right_diagonal_up(x, y):
    """ Move right diagonal up on the grid """
    return x + 1, y + 1


def move_left_diagonal_up(x, y):
    """ Move left diagonal up on the grid """
    return x - 1, y + 1


def move_right_diagonal_down(x, y):
    """ Move right diagonal down the grid """
    return x + 1, y - 1


def move_left_diagonal_down(x, y):
    """ Move left diagonal down on the grid """
    return x - 1, y - 1
