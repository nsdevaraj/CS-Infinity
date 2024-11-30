

sudoku_board_test_cases = [
    # Case 1: Valid Sudoku board
    {
        "name": "Valid Sudoku",
        "input": [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ],
        "expected": True,
    },
    # Case 2: Invalid board with duplicate in a row
    {
        "name": "Duplicate in Row",
        "input": [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".","2",".","2","8","."],  # Duplicate '2' in this row
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ],
        "expected": False,
    },
    # Case 3: Invalid board with duplicate in a column
    {
        "name": "Duplicate in Column",
        "input": [
            ["5","3",".",".","7",".","2",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
                                     # Duplicate '2' in this column
        ],
        "expected": False,
    },
    # Case 4: Invalid board with duplicate in a 3x3 sub-box
    {
        "name": "Duplicate in Sub-box",
        "input": [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9",".",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".","5",".","2","8","."],  # Duplicate '5' in this sub-box
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8","5",".","7","9"]
        ],
        "expected": False,
    },
    # Case 5: Board with empty cells (valid)
    {
        "name": "Valid with Empty Cells",
        "input": [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ],
        "expected": True,
    },
    # Case 6: All cells filled but invalid box
    {
        "name": "Fully Filled Invalid Board box",
        "input": [
            ["5","3","4","6","7","8","9","1","2"],
            ["6","7","2","1","9","5","3","4","8"],
            ["1","9","8","3","4","2","5","6","7"],
            ["8","5","9","7","6","1","4","2","3"],
            ["4","2","6","8","5","3","7","9","1"],
            ["7","1","3","9","2","4","8","5","6"],
            ["9","6","1","5","3","7","2","8","4"],
            ["2","8","7","4","1","9","6","9","5"], # Duplicate '9' in the last box
            ["3","4","5","2","8","6","1","7","9"]
        ],
        "expected": False,
    },
    # Case 7: Completely empty board (valid)
    {
        "name": "Completely Empty Board",
        "input": [
            [".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","."]
        ],
        "expected": True,
    },
    # Case 8: Maximum size filled (valid) - testing performance
    {
        "name": "Performance Test - Max Size Valid",
        "input": [
            ["1","2","3","4","5","6","7","8","9"],
            ["4","5","6","7","8","9","1","2","3"],
            ["7","8","9","1","2","3","4","5","6"],
            ["2","3","4","5","6","7","8","9","1"],
            ["5","6","7","8","9","1","2","3","4"],
            ["8","9","1","2","3","4","5","6","7"],
            ["3","4","5","6","7","8","9","1","2"],
            ["6","7","8","9","1","2","3","4","5"],
            ["9","1","2","3","4","5","6","7","8"],
        ],
        "expected": True,
    },
]


def test_sudoku_board(func):
    print(f"Testing function: {func.__name__}")

    for i, test_case in enumerate(sudoku_board_test_cases, 1):
        input_data = test_case["input"]
        expected_result = test_case["expected"]
        case_name = test_case["name"]

        result = func(input_data)

        # Check if the returned result matches the expected result
        assert (
            result == expected_result
        ), f"Test case ({case_name}) failed: expected {expected_result}, got {result}"

    print("All test cases passed!")







def is_valid_sudoku_1(board):
    # Create sets to track seen numbers
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num != '.':
                # Calculate the box index
                box_index = (r // 3) * 3 + (c // 3)

                # Check for duplicates
                if (num in rows[r] or
                    num in cols[c] or
                    num in boxes[box_index]):
                    return False

                # Add the number to the respective sets
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_index].add(num)

    return True

def is_valid_sudoku_2(two_d_array:list[list[str]])-> bool:
    tow_d_array_len, two_d_array_elm_len = len(two_d_array), len(two_d_array[0])

    col_set_lst:list[set[str]]= [set() for _ in range(two_d_array_elm_len)]
    sub_box_set_lst:list[set[str]] = []

    for i in range(tow_d_array_len):

        row_set:set[str] = set()
        if(i%3==0):
            sub_box_set_lst = [set() for _ in range(len(two_d_array[0])//3)]

        for j in range(two_d_array_elm_len):

            col_set = col_set_lst[j]
            sub_box_set = sub_box_set_lst[j//3]

            cell = two_d_array[i][j]
            if(cell == '.'):
                continue
            elif(cell in row_set or cell in col_set or cell in sub_box_set):
                return False
            else:
                row_set.add(cell)
                col_set.add(cell)
                sub_box_set.add(cell)

    return True




def is_valid_sudoku_3(board:list[list[str]])-> bool:

    def is_valid_in_row(board:list[list[str]], row_index: int, col_index:int, value: str )-> bool :
        row_lst = board[row_index]
        filtered_row_lst = row_lst[:col_index] + row_lst[col_index + 1:]
        return value not in filtered_row_lst


    def is_valid_in_col(board:list[list[str]],   row_index: int,col_index:int, value: str)-> bool :
        filtered_col_lst = [board[r][col_index] for r in range(len(board)) if r != row_index]
        return value not in filtered_col_lst


    def is_valid_in_box(board:list[list[str]],   row_index: int,col_index:int, value: str)-> bool :

        box_row_start_index:int = (row_index // 3) * 3
        box_row_end_index:int = box_row_start_index + 3

        box_col_start_index:int = (col_index // 3) * 3
        box_col_end_index:int = box_col_start_index + 3

        box_value_set = set()

        for i in range(box_row_start_index, box_row_end_index ):
            for j in range(box_col_start_index, box_col_end_index):
                if(i == row_index and j == col_index):
                    continue
                box_value_set.add(board[i][j])

        return value not in box_value_set




    def is_valid_cell(board:list[list[str]], row_index: int, col_index:int )-> bool :
        cell_value = board[row_index][col_index]
        if(cell_value == "."):
            return True
        elif(not is_valid_in_row(board, row_index, col_index, cell_value)):
            return False
        elif(not is_valid_in_col(board, row_index, col_index, cell_value)):
            return False
        elif(not is_valid_in_box(board, row_index, col_index, cell_value)):
            return False
        else:
            return True



    for i in range(9):
        for j in range(9):
            if(not is_valid_cell(board, i, j)):
                return False
    return True

# from chatGPT
# def is_valid_sudoku(board: list[list[str]]) -> bool:

#     def is_valid_in_row(row: list[str], value: str) -> bool:
#         return row.count(value) == 0

#     def is_valid_in_col(board: list[list[str]], col_index: int, value: str) -> bool:
#         return all(board[r][col_index] != value for r in range(9))

#     def is_valid_in_box(board: list[list[str]], row_index: int, col_index: int, value: str) -> bool:
#         box_row_start = (row_index // 3) * 3
#         box_col_start = (col_index // 3) * 3

#         return all(
#             board[i][j] != value
#             for i in range(box_row_start, box_row_start + 3)
#             for j in range(box_col_start, box_col_start + 3)
#             if (i, j) != (row_index, col_index)
#         )

#     for i in range(9):
#         for j in range(9):
#             cell_value = board[i][j]
#             if cell_value == ".":
#                 continue
#             if not (is_valid_in_row(board[i], cell_value) and
#                     is_valid_in_col(board, j, cell_value) and
#                     is_valid_in_box(board, i, j, cell_value)):
#                 return False

#     return True


def is_valid_sudoku_4(board: list[list[str]]) -> bool:

    def is_valid_in_row(row: list[str], value: str) -> bool:
        return row.count(value) == 1

    def is_valid_in_col(board: list[list[str]], col_index: int, value: str) -> bool:
        return [board[r][col_index] for r in range(9)].count(value) == 1

    def is_valid_in_box(board: list[list[str]], row_index: int, col_index: int, value: str) -> bool:
        box_row_start = (row_index // 3) * 3
        box_col_start = (col_index // 3) * 3

        return [
            board[i][j]
            for i in range(box_row_start, box_row_start + 3)
            for j in range(box_col_start, box_col_start + 3)
        ].count(value) == 1

    for i in range(9):
        for j in range(9):
            cell_value = board[i][j]
            if cell_value == ".":
                continue
            if not (is_valid_in_row(board[i], cell_value) and
                    is_valid_in_col(board, j, cell_value) and
                    is_valid_in_box(board, i, j, cell_value)):
                return False

    return True


test_sudoku_board(is_valid_sudoku_4)
