class InvalidBoardException(Exception):
    pass


class KnightAlreadyPresentException(InvalidBoardException):
    pass


class InvalidPositionException(InvalidBoardException):
    pass


class Board:
    def __init__(self, *, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols
        self.knight_position = None

    def is_valid_position(self, row: int, col: int) -> bool:
        return row in range(self.rows) and col in range(self.cols)

    def place_knight(self, row: int, col: int) -> None:
        if not self.is_valid_position(row, col):
            raise InvalidPositionException(f"Knight must be placed on a {self.rows} by {self.cols} board")
        if self.knight_position is not None:
            raise KnightAlreadyPresentException("Knight already present on the board")
        self.knight_position = (row, col)

    def get_possible_knight_moves(self) -> list[tuple[int, int]]:
        ...
