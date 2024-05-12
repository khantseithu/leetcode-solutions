from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Given an m x n grid of characters board and a string word, return true if word exists in the grid.

        The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
        """
        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            tmp, board[i][j] = board[i][j], '/'
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = tmp
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False

# Time complexity: O(N * 4^L) where N is the number of cells in the board and L is the length of the word to be matched.
# Space complexity: O(L) where L is the length of the word to be matched.

import unittest

class TestWordSearch(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_exist(self) -> None:
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "ABCCED"
        self.assertTrue(self.solution.exist(board, word))
        word = "SEE"
        self.assertTrue(self.solution.exist(board, word))
        word = "ABCB"
        self.assertFalse(self.solution.exist(board, word))
        board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
        word = "ABCESEEEFS"
        self.assertTrue(self.solution.exist(board, word))

if __name__ == '__main__':
    unittest.main()
