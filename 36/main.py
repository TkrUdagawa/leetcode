from typing import List

def get_box_index(i, j):
    if i < 3 and j < 3:
        return 0
    elif i < 3 and j < 6:
        return 1
    elif i < 3 and j < 9:
        return 2
    elif i < 6 and j < 3:
        return 3
    elif i < 6 and j < 6:
        return 4
    elif i < 6 and j < 9:
        return 5
    elif i < 9 and j < 3:
        return 6
    elif i < 9 and j < 6:
        return 7
    else:
        return 8

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [{} for _ in range(9)] 
        boxes = [{} for _ in range(9)] 
        for i, r in enumerate(board):
            row = {}
            for j, m in enumerate(r):
                if m != ".":
                    row[m] = row.get(m, 0) + 1
                    if row[m] > 1:
                        return False
                    columns[j][m] = columns[j].get(m, 0) + 1
                    if columns[j][m] > 1:
                        return False
                    idx = get_box_index(i, j)
                    boxes[idx][m] = boxes[idx].get(m, 0) + 1
                    if boxes[idx][m]  > 1:
                        return False
        return True
                
        
if __name__ == "__main__":
    c = Solution()
    board = [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    assert c.isValidSudoku(board)
    
    
    board = [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    assert not c.isValidSudoku(board)