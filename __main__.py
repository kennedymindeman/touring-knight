import timeit
from src.touring_knight import KnightTourSolver


def main():
    number_of_times = 100
    print(f"{timeit.timeit(solve, number=number_of_times) / number_of_times:.2e}[seconds]")
    print(solve().move_stack)


def solve():
    board = KnightTourSolver(rows=8, cols=8)
    board.place_knight(1, 1)
    board.solve()
    return board


if __name__ == "__main__":
    main()
