from collections import defaultdict

class Sudoku:
    def validate_entry(self,r,c,entry,board,row,col,box):
        if str(entry) in row[r].union(col[c].union(box[(r//3,c//3)])): return False
        else: return True
    
    
    def helper(self,board,row,col,box):
        for r in range(self.size):
            for c in range(self.size):
                if board[r][c]=='.':
                    for entry in range(1,10):
                        #If its valid based on the board in this particular state
                        if self.validate_entry(r,c,entry,board,row,col,box):#add the entry to the board
                            row[r].add(str(entry))
                            col[c].add(str(entry))
                            box[(r//3,c//3)].add(str(entry))
                            board[r][c]=str(entry)
                            # print(board[r][c])
                            if self.helper(board,row,col,box): return True #board is solved
                            row[r].remove(str(entry))
                            col[c].remove(str(entry))
                            box[(r//3,c//3)].remove(str(entry))
                            board[r][c]='.'
                    return False #Gets out of a tight spot
        return True
                        
            
    def solveSudoku(self, board):

        #Initialize all-- we don't want it to be global, so each iteration has different state
        row,col,box=defaultdict(set),defaultdict(set),defaultdict(set)
        self.size=9
        #Initialize all the present values given into the sets..
        for r in range(self.size):
            for c in range(self.size):
                if board[r][c].isnumeric():#adds only the numeric values to the sets.
                    row[r].add(board[r][c])
                    col[c].add(board[r][c])
                    box[(r//3,c//3)].add(board[r][c])
                    
        self.helper(board,row,col,box)# Where we solve the board
        print(board)

obj=Sudoku()
obj.solveSudoku(
[["1",".",".",".","7",".",".","3","."],
["8","3",".","6",".",".",".",".","."],
[".",".","2","9",".",".","6",".","8"],
["6",".",".",".",".","4","9",".","7"],
[".","9",".",".",".",".",".","5","."],
["3",".","7","5",".",".",".",".","4"],
["2",".","3",".",".","9","1",".","."],
[".",".",".",".",".","2",".","4","3"],
[".","4",".",".","8",".",".",".","9"]])