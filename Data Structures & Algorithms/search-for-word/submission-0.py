class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        char_set = set()
        flag = []
        def check(pos, char_num):
            #pos = [row - 1, col - 1]
            if  char_num == len(word):
                return True
            row, col = pos[0], pos[1]
            #4 options up down left right
            #down
            if row - 1 >= 0 and board[row -1][col] == word[char_num] and not((row -1,col) in char_set):
                temp_pos = (row-1, col)
                char_set.add(temp_pos)
                if check(temp_pos, char_num + 1):
                    return True
                char_set.remove(temp_pos)
            #up
            if row + 1 < len(board) and board[row+ 1][col] == word[char_num] and not((row +1,col) in char_set):
                temp_pos = (row + 1, col)
                char_set.add(temp_pos)
                if check(temp_pos, char_num + 1):
                    return True
                char_set.remove(temp_pos)
            #left
            if col - 1 >= 0 and board[row][col - 1] == word[char_num] and not((row,col -1) in char_set):
                temp_pos = (row, col - 1)
                char_set.add(temp_pos)
                if check(temp_pos, char_num + 1):
                    return True
                char_set.remove(temp_pos)
            #right
            if col + 1 < len(board[0]) and board[row][col + 1 ] == word[char_num] and not((row,col + 1) in char_set):
                temp_pos = (row, col + 1)
                char_set.add(temp_pos)
                if check(temp_pos, char_num + 1):
                    return True
                char_set.remove(temp_pos)

            return False

        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if board[i][j] == word[0]:
                    char_set.add((i,j))
                    if check((i, j), 1):
                        return True
                    char_set.remove((i,j))

        return False

