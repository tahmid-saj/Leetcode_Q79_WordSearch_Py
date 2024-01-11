class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
      for i in range(len(board)):
        for j in range(len(board[0])):
          if board[i][j] == word[0]:
            if self.backtrack(board, word, 0, i, j): return True
      return False
    
    def backtrack(self, board, word, index, i, j):
      if index == len(word): return True
      if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]): return False

      if board[i][j] != word[index]: return False
      tmp, board[i][j] = board[i][j], "/"

      if self.backtrack(board, word, index + 1, i - 1, j): return True
      if self.backtrack(board, word, index + 1, i + 1, j): return True
      if self.backtrack(board, word, index + 1, i, j - 1): return True
      if self.backtrack(board, word, index + 1, i, j + 1): return True

      board[i][j] = tmp

      return False
