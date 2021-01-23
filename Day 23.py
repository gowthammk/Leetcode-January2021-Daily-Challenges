# Sort the Matrix Diagonally
#
# Solution
# A matrix diagonal is a diagonal line of cells starting from some cell in either the
# topmost row or leftmost column and going in the bottom-right direction until reaching
# the matrix's end. For example, the matrix diagonal starting from mat[2][0],
# where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].
#
# Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order
# and return the resulting matrix.
#
#
#
# Example 1:
#
#
# Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
# Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
#
#
# Constraints:
#
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# 1 <= mat[i][j] <= 100

class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n, d = len(mat), len(mat[0]), defaultdict(list)
        for i in range(m):
            for j in range(n):
                d[j - i].append(mat[i][j])

        for k in d:
            for i, num in enumerate(sorted(d[k])):
                mat[i + max(-k, 0)][k + i + max(-k, 0)] = num

        return mat