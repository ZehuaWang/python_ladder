import math
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        board_size = 9
        for i in range(board_size):
            rows_list = []
            cols_list = []
            cube_list = []
            
            for j in range(board_size):

                # decide if the row has duplicate number
                if board[i][j] != "." and board[i][j] not in rows_list:
                    rows_list.append(board[i][j])
                elif board[i][j] != "." and board[i][j] in rows_list: 
                    return False
                else:
                    pass
               
                # decide if the col has duplicate number
                if board[j][i] != "." and board[j][i] not in cols_list:
                    cols_list.append(board[j][i])
                elif board[j][i] != "." and board[j][i] in cols_list:
                    return False
                else:
                    pass
                
                # decide if the cube has duplicate number
                row_index = 3 * (i //3)
                col_index = 3 * (i % 3)
                if row_index + j//3 <= 8 and col_index + j%3 <= 8:
                    if board[row_index + j//3][col_index + j%3] != "." and board[row_index + j//3][col_index + j%3] not in cube_list:
                        cube_list.append(board[row_index + j//3][col_index + j%3])
                    elif board[row_index + j//3][col_index + j%3] != "." and board[row_index + j//3][col_index + j%3] in cube_list:
                        return False
                    else:
                        pass
                
        return True
            