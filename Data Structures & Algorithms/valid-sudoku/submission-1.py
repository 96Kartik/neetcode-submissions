class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_count = len(board)
        col_count = len(board[0])
        #Row Check
        for row in board:
            row_digit_list = [i for i in row if i != "."]
            row_digit_set = set(row_digit_list)
            if len(row_digit_list) != len(row_digit_set):
                return False
        
        #Column Check
        for col in range(col_count):
            column_digit_list = []
            for row in range(col_count):
                if board[row][col] != ".":
                    column_digit_list.append(board[row][col])
            column_digit_set = set(column_digit_list)
            if len(column_digit_list) != len(column_digit_set):
                return False

        #sub-box Checks
        grids = [
            [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)],
            [(0,3), (0,4), (0,5), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5)],
            [(0,6), (0,7), (0,8), (1,6), (1,7), (1,8), (2,6), (2,7), (2,8)],
            [(3,0), (3,1), (3,2), (4,0), (4,1), (4,2), (5,0), (5,1), (5,2)],
            [(3,3), (3,4), (3,5), (4,3), (4,4), (4,5), (5,3), (5,4), (5,5)],
            [(3,6), (3,7), (3,8), (4,6), (4,7), (4,8), (5,6), (5,7), (5,8)],
            [(6,0), (6,1), (6,2), (7,0), (7,1), (7,2), (8,0), (8,1), (8,2)],
            [(6,3), (6,4), (6,5), (7,3), (7,4), (7,5), (8,3), (8,4), (8,5)],
            [(6,6), (6,7), (6,8), (7,6), (7,7), (7,8), (8,6), (8,7), (8,8)],
        ]

        grid_digits = [[board[g[0]][g[1]] for g in grid if board[g[0]][g[1]] != "."] for grid in grids]
        grid_sets = [set(g) for g in grid_digits]

        for i in range(len(grid_digits)):
            if len(grid_digits[i]) != len(grid_sets[i]):
                return False
        
        return True


        