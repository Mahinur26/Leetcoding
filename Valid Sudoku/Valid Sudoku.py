#Medium

import collections
#Optimal Solution
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Ensures that if the val isn't in the set, it will add it
        #Normal sets don't add new values when you try to access it
        #A dictionary with sets as its key
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        #3 by 3 grid
        square = collections.defaultdict(set) #[row//3,col//3]:val
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                #If the val has already occured in the current row/col/square, then return false
                #Remember the key is [row//3,col//3]
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or 
                board[r][c] in square[r//3,c//3]):
                    return False
                #Adding the new value in each of the current set being accessed
                #Must use add() function
                #If the dictionary key DNE, then it is created and the board[r][c] is added to the key/set()
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                square[r//3,c//3].add(board[r][c])
        
        return True
    
    #Space complexity = O(n^2)
    #Time complexity = O(n^2)