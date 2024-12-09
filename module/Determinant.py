from typing import List


class Determinant:
    @staticmethod
    def is_square(matrix: List[List[int]]) -> bool:
        """
        정방 행렬
        """
        return len(matrix) == len(matrix[0])

    @staticmethod
    def determinant(matrix: List[List[int]]) -> int:
        """
        판별식
        """
        if len(matrix) == 1:
            return matrix[0][0]

        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        det = 0
        for col in range(len(matrix)):
            minor = [row[:col] + row[col + 1 :] for row in matrix[1:]]
            sign = (-1) ** col
            det += sign * matrix[0][col] * Determinant.determinant(minor)

        return det

    @staticmethod
    def is_invertible(matrix: List[List[int]]) -> bool:
        """
        가역 행렬
        """
        if not Determinant.is_square(matrix):
            return False

        return Determinant.determinant(matrix) != 0
