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
    pass

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
    This function checks the board to see if there are any duplicate numbers in a box.
    >>> check_in_box([\
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
    pass

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
