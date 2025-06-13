class Board:
    def __init__(self, *, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols

    def is_valid_position(self, row: int, col: int) -> bool:
        return row in range(self.rows) and col in range(self.cols)
