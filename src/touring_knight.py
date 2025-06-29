class InvalidBoardException(Exception):
    pass


class KnightAlreadyPresentException(InvalidBoardException):
    pass


class InvalidPositionException(InvalidBoardException):
    pass


class NoKnightOnBoardException(InvalidBoardException):
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
        self.knight_position = None

    def is_valid_position(self, row: int, col: int) -> bool:
        return (
            row in range(self.rows) and
            col in range(self.cols) and
            (row, col) not in self.visited
        )

    def place_knight(self, row: int, col: int) -> None:
        if not self.is_valid_position(row, col):
            raise InvalidPositionException(f"Knight must be placed on a {self.rows} by {self.cols} board")
        if self.knight_position is not None:
            raise KnightAlreadyPresentException("Knight already present on the board")
        self.knight_position = (row, col)
        self.visited.add((row, col))

    def get_possible_knight_moves(self) -> list[tuple[int, int]]:
        if self.knight_position is None:
            raise NoKnightOnBoardException("There must be a knight on the board to move it")
        valid_next_positions = []
        row, col = self.knight_position
        for row_offset, col_offset in Board.KNIGHT_OFFSETS:
            valid_next_position = (row + row_offset, col + col_offset)
            if self.is_valid_position(*valid_next_position):
                valid_next_positions.append(valid_next_position)
        return valid_next_positions

    def move_knight(self, row: int, col: int) -> None:
        if (row, col) not in self.get_possible_knight_moves():
            raise InvalidKnightMove(f"Knight cannot move from {self.knight_position} to {(row, col)}")
        self.knight_position = (row, col)
        self.visited.add((row, col))
