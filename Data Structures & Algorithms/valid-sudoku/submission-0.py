class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            seen = [0 for x in range(9)]
            for i in row:
                if not i == ".":
                    seen[int(i) - 1] += 1
                    if seen[int(i) - 1] > 1:
                        return False
                
        for col in range(len(board[0])):
            seen = [0 for x in range(9)]
            for row in range(len(board)):
                square = board[row][col]
                if not square == ".":
                    seen[int(square) - 1] += 1
                    if seen[int(square) - 1] > 1:
                        return False

        top_left_corner = [0,0]
        for square in range(9):
            seen = [0 for x in range(9)]
            for y in range(3):
                for x in range(3):
                    space = board[top_left_corner[1]+y][top_left_corner[0]+x]
                    if not space == ".":
                        seen[int(space)-1] += 1
                        if seen[int(space)-1] > 1:
                            return False
            if top_left_corner[0] == 6:
                top_left_corner[0] = 0
                top_left_corner[1] += 3
            else:
                top_left_corner[0] += 3
        
        return True
