from module.Equation import Equation


class EquationFactory:
    @staticmethod
    def create() -> Equation:
        # TODO: input 하드코딩
        # rows = int(input('식의 개수: '))
        # equations = [input(f'{i+1}번째 방정식: ') for i in range(rows)]
        equations = [
            "x + y + z + w = 10",
            "2x + 2y + 2z + 2w = 20",  # 첫 번째 식의 배수
            "x - y + z - w = 5",
            "2x - 2y + 2z - 2w = 10"  # 세 번째 식의 배수
        ]

        return Equation(equations)
