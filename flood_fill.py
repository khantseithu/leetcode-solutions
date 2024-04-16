
from typing import List
import unittest

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).
        Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.
        To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on.
        Replace the color of all of the aforementioned pixels with the newColor.
        """
        if image[sr][sc] == color:
            return image
        self.fill(image, sr, sc, image[sr][sc], color)
        return image

    def fill(self, image: List[List[int]], r: int, c: int, color: int, newColor: int) -> None:
        if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != color:
            return
        image[r][c] = newColor
        self.fill(image, r + 1, c, color, newColor)
        self.fill(image, r - 1, c, color, newColor)
        self.fill(image, r, c + 1, color, newColor)
        self.fill(image, r, c - 1, color, newColor)

# Time complexity: O(n)
# Space complexity: O(n)

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_floodFill(self):
        self.assertEqual(self.solution.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2), [[2,2,2],[2,2,0],[2,0,1]])
        self.assertEqual(self.solution.floodFill([[0,0,0],[0,1,1]], 1, 1, 1), [[0,0,0],[0,1,1]])

if __name__ == '__main__':
    unittest.main()
