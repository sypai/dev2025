"""
🔁 Problem: Transpose Matrix
Write a function that takes in a 2D array (a matrix) and returns its transpose.

The transpose of a matrix is a flipped version where the rows become columns and columns become rows.

📥 Input
A 2D list of integers: matrix: List[List[int]]

All rows are of the same length

📤 Output
A new 2D list representing the transpose

🧠 Example 1:

Input:
matrix = [
  [1, 2],
  [3, 4],
  [5, 6]
]

Output:
[
  [1, 3, 5],
  [2, 4, 6]
]
"""

# Time Complexity : O(rows x columns) | Space : O(rows x columns)
# Took me 22 mins
def transpose_matrix(matrix):
    matrixRows = len(matrix)
    if matrixRows == 0:
        return []
    matrixColumns = len(matrix[0])

    transposed = [[0 for _ in range(matrixRows)] for _ in range(matrixColumns)]
   
    for i in range(matrixColumns):
        for j in range(matrixRows):
            transposed[i][j] = matrix[j][i]
    return transposed

def transpose_square_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):  # Only swap above-diagonal
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


if __name__ == "__main__":
    matrix = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]
    print(transpose_matrix(matrix))

    square = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(transpose_square_matrix(square))
