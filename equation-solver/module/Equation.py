import re
from typing import List, Tuple

from module.Determinant import Determinant
from module.InverseMatrix import InverseMatrix


class Equation:
    __COEFFICIENT_PATTERN = re.compile(r"([+-]?\d*(?:\.\d+)?)\s*([a-z]+)")

    def __init__(self, equations: List[str]):
        self.equations = list(map(lambda s: s.lower(), equations))
        self.variables = self.__parse_variables(self.equations)
        self.coefficients, self.answer = self.__parse_equations(
            self.equations, self.variables
        )

    def __str__(self) -> str:
        return f"계수행렬: {self.coefficients}, 상수 벡터: {self.answer}"

    @staticmethod
    def __parse_variables(equations: List[str]) -> List[str]:
        """
        전체 식에서 변수 추출
        """
        result = set()

        for equation in equations:
            result |= set(re.findall(r"[a-z]+", equation))

        return list(sorted(result))

    @staticmethod
    def __parse_equations(
            equations: List[str], variables: List[str]
    ) -> Tuple[List[List[int]], List[int]]:
        """
        전체 식 파싱
        :return: (계수 행렬, 상수 벡터)
        """
        _coefficients = []
        _answers = []

        for equation in equations:
            coefficients = {}

            raw_coefficient, raw_answer = equation.split("=")
            matches = Equation.__COEFFICIENT_PATTERN.findall(raw_coefficient)

            for match in matches:
                coefficients[match[1]] = (
                    int(match[0])
                    if match[0] not in ("", "+", "-")
                    else int(f"{match[0]}1")
                )

            _coefficients.append([coefficients[var] for var in variables])
            _answers.append(int(raw_answer))

        return _coefficients, _answers

    def solve(self):
        if Determinant.is_invertible(self.coefficients):
            solution = []

            inverse_matrix = InverseMatrix.inverse(self.coefficients)
            for i in range(len(inverse_matrix)):
                value = 0
                for j in range(len(self.answer)):
                    value += inverse_matrix[i][j] * self.answer[j]
                solution.append(value)

            return solution
        else:
            # 비가역 행렬일 경우
            pass