"""This module contains the functions for validating the board and checking for a win."""
def validate_board(board: list) -> bool:
    """
    This function validates the board to ensure that it is a valid board.
    >>> validate_board([\
 "**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   1  **",\
 "  8  2***",\
 "  2  ****"])
    False
    """
    return check_in_row(board) and check_in_col(board) and check_in_box(board)

def check_in_row(board: list) -> bool:
    """
    This function checks the board to see if there are any duplicate numbers in a row.
    >>> check_in_row([\
 "**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   1  **",\
 "  8  2***",\
 "  2  ****"])
    True
    """
    for i in board:
        for j in i:
            if j != "*" and j != ' ' and i.count(j) > 1:
                return False
    return True

def check_in_col(board: list) -> bool:
    """
    This function checks the board to see if there are any duplicate numbers in a column.
    >>> check_in_col([\
 "**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   1  **",\
 "  8  2***",\
 "  2  ****"])
    False
    """
    for i in range(9):
        col = []
        for j in range(9):
            col.append(board[j][i])
        for k in col:
            if k != "*" and k != ' ' and col.count(k) > 1:
                return False
    return True

def check_in_box(board: list) -> bool:
    """
    This function checks the board to see if there are any duplicate numbers in a L shaped 5x5 box.
    >>> check_in_box([\
 "**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  82  *",\
 "3   1  **",\
 "  8  2***",\
 "  2  ****"])
    True
    """
    co = 8
    count = 0
    cou = 4
    for j in range(4,9):
        box = []
        for k in range(5):
            box.append(board[k+count][cou])
        for l in range(5):
            box.append(board[j][co-l])
        for m in box:
            if m != "*" and m != ' ' and box.count(m) > 1:
                return False
        count += 1
        co -= 1
        cou -= 1
    return True

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
