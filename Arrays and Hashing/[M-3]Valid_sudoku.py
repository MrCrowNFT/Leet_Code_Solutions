# Valid Sudoku
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be 
# validated according to the following rules:

#Each row must contain the digits 1-9 without repetition.
#Each column must contain the digits 1-9 without repetition.
#Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
#Note:
#A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#Only the filled cells need to be validated according to the mentioned rules.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # We need to look for dups in columns, rows and squares, therfore
        # a hashmap for each to check for them
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  

        for r in range(9):
            for c in range(9):
            # check in every position (every index), we skip the . values as they are empty
                if board[r][c] == ".":
                    continue
            # if the value is already in columns or rows or square is a dup an we reject the board, 
            # to get the square we divide and round down the index (so if index 1,2, we know is in 
            # the square 0,0)
                if ( board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                # If is not dup we update the hashmaps
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True
