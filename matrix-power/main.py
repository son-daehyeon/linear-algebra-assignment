from module.Matrix import Matrix


if __name__ == "__main__":
    N, M = map(int, input("행렬의 행과 열의 개수를 입력하세요 (공백 구분): ").split())
    K = int(input("거듭제곱할 지수를 입력하세요: "))
    A = []

    for i in range(1, N + 1):
        row = list(map(int, input(f"{i}행 입력 (공백 구분): ").split()))

        if len(row) != M:
            raise Exception("행렬의 열의 개수가 올바르지 않습니다.")

        A.append(row)

    print(Matrix(N, M, A).power(K))