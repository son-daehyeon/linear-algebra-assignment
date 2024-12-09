from typing import List
from module.Determinant import Determinant


class InverseMatrix:
    @staticmethod
    def cofactor(matrix: List[List[int]]) -> List[List[int]]:
        """여인수 행렬"""
        cofactors = []

        for r in range(len(matrix)):
            cofactor_row = []
            for c in range(len(matrix)):
                minor = [
                    row[:c] + row[c + 1 :] for row in (matrix[:r] + matrix[r + 1 :])
                ]
                cofactor_row.append(((-1) ** (r + c)) * Determinant.determinant(minor))
            cofactors.append(cofactor_row)

        return cofactors

    @staticmethod
    def transpose(matrix: List[List[int]]) -> List[List[int]]:
        """전치 행렬"""
        return [list(row) for row in zip(*matrix)]

    @staticmethod
    def inverse(matrix: List[List[int]]) -> List[List[float]]:
        """역행렬"""
        det = Determinant.determinant(matrix)
        cofactors = InverseMatrix.cofactor(matrix)
        transpose = InverseMatrix.transpose(cofactors)

        return [[elem / det for elem in row] for row in transpose]
