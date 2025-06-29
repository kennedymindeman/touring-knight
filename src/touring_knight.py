class InvalidBoardException(Exception):
    pass


class InvalidPositionException(InvalidBoardException):
    pass


class InvalidKnightMove(InvalidBoardException):
    pass


class Board:
    KNIGHT_OFFSETS = (
        (1, 2), (-1, 2), (-1, -2), (1, -2),
        (2, 1), (-2, 1), (-2, -1), (2, -1),
    )

    def __init__(self, *, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols
        self.visited = set()
        self.move_stack = []
        self.knight_position = None

    def is_valid_position(self, row: int, col: int) -> bool:
        return (
            row in range(self.rows) and
            col in range(self.cols) and
            (row, col) not in self.visited
        )

    def get_possible_knight_moves(self, row: int, col: int) -> list[tuple[int, int]]:
        valid_next_positions = []
        for row_offset, col_offset in Board.KNIGHT_OFFSETS:
            valid_next_position = (row + row_offset, col + col_offset)
            if self.is_valid_position(*valid_next_position):
                valid_next_positions.append(valid_next_position)
        return valid_next_positions

    def place_knight(self, row: int, col: int) -> None:
        if self.knight_position is None and not self.is_valid_position(row, col):
            raise InvalidPositionException(f"Knight cannot be placed at {(row, col)}")
        if (
            self.knight_position and
            (row, col) not in self.get_possible_knight_moves(*self.knight_position)
        ):
            raise InvalidKnightMove(f"Knight cannot move from {self.knight_position} to {(row, col)}")
        self.knight_position = (row, col)
        self.visited.add(self.knight_position)
        self.move_stack.append(self.knight_position)

    def get_valid_moves_ordered_by_cost(self) -> list[tuple[int, int]]:
        if self.knight_position is None:
            possible_next_moves = self.get_list_of_all_board_tiles()
        else:
            possible_next_moves = self.get_possible_knight_moves(*self.knight_position)
        return sorted(
            possible_next_moves,
            key=lambda x: len(self.get_possible_knight_moves(*x)),
        )

    def solved(self) -> bool:
        return len(self.visited) == self.rows * self.cols

    def get_list_of_all_board_tiles(self) -> list[tuple[int, int]]:
        valid_next_positions = []
        for row in range(self.rows):
            valid_next_positions.extend((row, col) for col in range(self.cols))
        return valid_next_positions
