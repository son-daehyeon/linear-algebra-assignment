class Matrix:
    def __init__(self, n, m, rows):
        self.n = n
        self.m = m
        self.rows = rows

    def __str__(self):
        return '\n'.join([' '.join(str(value) for value in row) for row in self.rows])

    def __mul__(self, ref):
        if self.m != ref.n:
            raise Exception("행렬 곱셈 불가능: A의 열 수와 B의 행 수가 일치하지 않습니다.")

        return Matrix(self.n, ref.m, [[sum(self.rows[i][k] * ref.rows[k][j] for k in range(self.m)) for j in range(ref.m)] for i in range(self.n)])

    @staticmethod
    def identity_matrix(size):
        return [[1 if i == j else 0 for j in range(size)] for i in range(size)]

    def power(self, k):
        if self.n != self.m:
            raise Exception("거듭제곱 불가능: 정사각행렬만 가능합니다.")

        base = self
        result = Matrix(self.n, self.m, Matrix.identity_matrix(self.n))

        if k == 0:
            return result
        if k == 1:
            return self

        while k > 0:
            if k % 2 == 1:
                result *= base
            base *= base
            k //= 2

        return result