from src.touring_knight import Board


def main():
    board = Board(rows=10, cols=10)
    board.solve()
    print(board.move_stack)


if __name__ == "__main__":
    main()
