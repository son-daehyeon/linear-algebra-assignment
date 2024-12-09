from module.Equation import Equation


if __name__ == "__main__":
    rows = int(input('식의 개수: '))
    equations = [input(f'{i+1}번째 방정식: ') for i in range(rows)]

    print(Equation(equations).solve())