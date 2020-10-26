from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        A = matrix
        print(A)
        n = len(A)
        for i in range(n):
            for j in range(i):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        print(A)
        for row in A:
            for j in range(n // 2):
                row[j], row[~j] = row[~j], row[j]


if __name__ == '__main__':
    s = Solution()
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix = [[1, 2], [3, 4]]
    #matrix = [[1]]
    s.rotate(matrix)
    print(matrix)
    #sol_matrix = [[1]]
    sol_matrix = [[3, 1], [4, 2]]
    #sol_matrix = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    #sol_matrix = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
    assert matrix == sol_matrix
