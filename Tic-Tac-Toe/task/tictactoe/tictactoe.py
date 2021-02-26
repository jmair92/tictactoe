# write your code here
CELL_OCCUPIED = 'This cell is occupied! Choose another one!'
ASK_FOR_GRID = 'Enter cells:'
INVALID_COORDINATES_FORMAT = 'You should enter numbers!'
ASK_FOR_COORDINATES = 'Enter the coordinates:'
COORDINATES_LIMIT_EXCEEDED = 'Coordinates should be from 1 to 3!'
NOT_FINISHED = 'Game not finished'
DRAW = 'Draw'
X_CHAR = 'X'
X_LINE = X_CHAR + X_CHAR + X_CHAR
O_CHAR = 'O'
O_LINE = O_CHAR + O_CHAR + O_CHAR
X_WINS = f'{X_CHAR} wins'
O_WINS = f'{O_CHAR} wins'
IMPOSSIBLE = 'Impossible'
EMPTY = '_'
TOP_BORDER = '-'
SIDE_BORDER = '|'
ENDING_STATES = [X_WINS, O_WINS, DRAW, IMPOSSIBLE]


def print_border():
    top_border = ''
    for top_border_char in range(1, 10):
        top_border += TOP_BORDER

    print(top_border)


def print_lines(grid_string: str):
    chars = list(grid_string)
    for x in range(0, 3):
        get_line(chars, x)


def get_line(grid_chars, line_number):
    line = ''
    line += f'{SIDE_BORDER} '
    for y in range(0, 3):
        current_char = grid_chars[(3 * line_number) + y]
        line += f"{current_char} "

    line += SIDE_BORDER
    print(line)


def get_row_state(grid_chars: str, row_index):
    row_start = row_index * 3
    row_end = row_start + 3
    row = grid_chars[row_start:row_end]
    if row == X_LINE:
        return X_WINS
    if row == O_LINE:
        return O_WINS


def get_column_state(grid_chars: str, column_index: int):
    column = grid_chars[column_index] + grid_chars[column_index + 3] + grid_chars[column_index + 6]
    if column == X_LINE:
        return X_WINS
    if column == O_LINE:
        return O_WINS


def get_diagonals_state(grid_chars: str):
    first_diagonal = grid_chars[0] + grid_chars[4] + grid_chars[8]
    second_diagonal = grid_chars[2] + grid_chars[4] + grid_chars[6]

    if first_diagonal == X_LINE or second_diagonal == X_LINE:
        return X_WINS
    if first_diagonal == O_LINE or second_diagonal == O_LINE:
        return O_WINS


def is_played(cell: str):
    return (cell == X_CHAR) or (cell == O_CHAR)


def get_played_cells(grid_chars: str):
    return [cell for cell in grid_chars if is_played(cell)]


def get_not_finished(grid_chars: str):
    played_cells = get_played_cells(grid_chars)
    if len(played_cells) < 9:
        return NOT_FINISHED


def get_impossible_state(grid_chars: str):
    x_chars = [char for char in grid_chars if char == X_CHAR]
    o_chars = [char for char in grid_chars if char == O_CHAR]
    if abs(len(x_chars) - len(o_chars)) > 1:
        return IMPOSSIBLE

    rows_state = []
    columns_state = []
    for x in range(0, 3):
        row_state = get_row_state(grid_chars, x)
        if row_state is not None:
            rows_state.append(row_state)

    for y in range(0, 3):
        column_state = get_column_state(grid_chars, y)
        if column_state is not None:
            columns_state.append(column_state)

    won_lines = len(rows_state) + len(columns_state) > 1
    if won_lines:
        return IMPOSSIBLE


def get_state(grid_chars: str):
    impossible_state = get_impossible_state(grid_chars)
    if impossible_state is not None:
        return impossible_state

    for x in range(0, 3):
        row_state = get_row_state(grid_chars, x)
        if row_state is not None:
            return row_state

    for y in range(0, 3):
        column_state = get_column_state(grid_chars, y)
        if column_state is not None:
            return column_state

    diagonals_state = get_diagonals_state(grid_chars)
    if diagonals_state is not None:
        return diagonals_state

    not_finished = get_not_finished(grid_chars)
    if not_finished is not None:
        return not_finished

    return DRAW


def print_grid(grid_chars: str):
    print_border()
    print_lines(grid_chars)
    print_border()


def get_user_coordinates(grid_chars: str):
    x, y = None, None
    occupied = True
    invalid_coordinates = True

    while invalid_coordinates or occupied:
        coordinates = input(ASK_FOR_COORDINATES).split()
        x = int(coordinates[0])
        y = int(coordinates[1])
        invalid_coordinates = not isinstance(x, int) or not isinstance(y, int)

        if not(1 <= x <= 3) or not(1 <= y <= 3):
            print(COORDINATES_LIMIT_EXCEEDED)
        elif invalid_coordinates:
            print(INVALID_COORDINATES_FORMAT)
        else:
            occupied = grid_chars[coordinates_to_grid(x, y)] != EMPTY
            if occupied:
                print(CELL_OCCUPIED)

    return x, y


def coordinates_to_grid(x: int, y: int):
    grid_position = x - 1
    grid_position += (3 - y) * 3
    return grid_position


def apply_move(grid_chars: str, char: str, x: int, y: int):
    grid_list = list(grid_chars)
    grid_list[coordinates_to_grid(x, y)] = char
    return "".join(grid_list)


grid = '_________'
state = ''
current_player = X_CHAR

while state not in ENDING_STATES:
    print_grid(grid)
    user_x, user_y = get_user_coordinates(grid)
    grid = apply_move(grid, current_player, user_x, user_y)
    state = get_state(grid)
    current_player = X_CHAR if current_player == O_CHAR else O_CHAR

print_grid(grid)
print(state)
