class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=set()
        cols=set()
        box=set()
        for i in range(9):
         for j in range(9):
            if board[i][j]=='.':
               continue
            else:
               num=board[i][j]
            row_key=(i,num)
            if row_key not in rows:
             rows.add(row_key)
            else:
             return False
            col_key=(j,num)
            if col_key not in cols:
              cols.add(col_key)
            else:
              return False
            box_key=(i//3,j//3,num)
            if box_key not in box:
              box.add(box_key)
            else:
              return False
        return True
            