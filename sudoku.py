import sys


def controller(row, column, number, cells):
    # Controller function: Checks whether the specified number exists in the same row, column, and 3x3 square.
    for i in range(9):
        if cells[row][i] == number:
            return False

    for j in range(9):
        if cells[j][column] == number:
            return False

    rowCell = (row // 3) * 3
    columnCell = (column // 3) * 3

    for r in range(3):
        for c in range(3):
            if cells[rowCell + r][columnCell + c] == number:
                return False

    return True


def solver(cells, result, step=0):
    # Solves the Sudoku puzzle using the backtracking algorithm.
    possibilities = []
    counter = 1

    for row in range(9):
        for column in range(9):
            if cells[row][column] == 0:
                # We checked whether the determined position is empty or not.
                for number in range(1, 10):
                    counter += 1
                    if controller(row, column, number, cells):
                        possibilities.append(number)
                        if counter < 10:
                            number += 1
                        elif counter == 10:
                            if len(possibilities) == 1:
                                # Places the only possible value in the cell.
                                cells[row][column] = possibilities[0]
                                counter = 1
                                step += 1
                                a = (
                                    ("-" * 18) + "\n" +
                                    ("Step {} - {} @ R{}C{}".format(step, possibilities[0], row + 1,
                                                                    column + 1)) + "\n" +
                                    ("-" * 18) + "\n",
                                    [list(row) for row in cells]
                                )
                                result.append(a)
                                possibilities.clear()
                                # Recursively calls the solver function for the next step.
                                solver(cells, result, step)
                                return result
                            else:
                                # If there are multiple possible values, it moves on to the next empty cell.
                                possibilities.clear()
                                number = 0
                                counter = 1
                                continue
                    else:
                        # We added an additional conditional statement to handle exceptional cases as well.
                        if counter == 10:
                            if len(possibilities) == 1:
                                cells[row][column] = possibilities[0]
                                counter = 1
                                step += 1
                                a = (
                                    ("-" * 18) + "\n" +
                                    ("Step {} - {} @ R{}C{}".format(step, possibilities[0], row + 1,
                                                                    column + 1)) + "\n" +
                                    ("-" * 18) + "\n",
                                    [list(row) for row in cells]
                                )
                                result.append(a)
                                possibilities.clear()
                                # Recursively calls the solver function for the next step.
                                solver(cells, result, step)
                                return result
                            else:
                                # If there are multiple possible values, it moves on to the next empty cell.
                                counter = 1
                                possibilities.clear()


def main():
    # Reads input from a text document, solves the Sudoku puzzle, and writes the result to another text document.
    with open(sys.argv[1], "r") as f:
        cells = [list(map(int, row.split())) for row in f]

    result = []
    solver(cells, result)

    with open(sys.argv[2], "w") as o:
        for item in result:
            o.write(item[0])
            for row in item[1]:
                o.write(" ".join(map(str, row)) + "\n")
        o.write(("-" * 18))


if __name__ == "__main__":
    main()