import numpy as np
import pandas as pd
import plotly.express as px
import plotly.io as pio
pio.renderers.default = "browser"

'''
Made by: Muhammad Adhim Mulia
Student ID: 22220302
Email: adhimmuliam@gmail.com
Version: Beta.0.1 (Last Updated: 22 February 2022)

Sandbox 1
'''


class Simres:
    def __init__(self):
        # Initiation Variable
        self.dx = 300  # feet
        self.dt = 50  # days
        self.miu = 2  # cp
        self.ct = 5 * (10 ** -6)  # 1/psi
        self.porosity = 0.2  # fraction
        self.k = 10  # mD

        # Boundary
        self.pinit = 1000  # psi
        self.pfinal = 500  # psi

        # Metrics Size
        self.x = 10
        self.nday = 33

    def explicit(self):
        self.matrix = np.zeros((self.nday + 1, self.x), dtype=float)
        self.beta = (0.00026368 * self.k / (self.porosity * self.ct * self.miu)) * (self.dt / (self.dx ** 2))
        self.matrix[0, :] = self.pinit
        self.matrix[0, -1] = self.pfinal
        self.matrix[:, 0] = self.pinit

        for index_row, row in enumerate(self.matrix):
            if index_row == 0:
                continue
            for index_column, column in enumerate(row):
                if index_column == 0:
                    self.matrix[index_row, index_column] = self.matrix[0, 0]
                    continue
                if index_column == len(self.matrix[0]) - 1:
                    self.matrix[index_row, index_column] = self.matrix[0, -1]
                    continue
                n_min1 = self.matrix[index_row - 1, index_column - 1]
                n = self.matrix[index_row - 1, index_column]
                n_plus1 = self.matrix[index_row - 1, index_column + 1]
                self.matrix[index_row, index_column] = (self.beta * n_min1) - ((2 * self.beta - 1) * n) + (
                        self.beta * n_plus1)

        column = list(range(1, self.x + 1))
        rows = np.array(list(range(0, self.nday + 1)))
        days = rows * self.dt
        df_explicit = pd.DataFrame(data=self.matrix, columns=column)
        df_explicit.index = days

        return df_explicit

    def implicit(self):
        self.beta = (0.00026368 * self.k / (self.porosity * self.ct * self.miu)) * (self.dt / (self.dx ** 2))
        value_of_mid_diagonal = (-1)*(2*self.beta+1)
        value_of_above_diagonal = self.beta
        value_of_below_diagonal = self.beta

        # Creating matrix A
        matrix_a = self.create_tridiagonal_matrix(size_of_a_matrix=(self.x-2),
                                                  value_for_diagonal=value_of_mid_diagonal,
                                                  value_for_above_diagonal=value_of_above_diagonal,
                                                  value_for_below_diagonal=value_of_below_diagonal)
        # Inverting matrix A
        matrix_a_inverted = np.linalg.inv(matrix_a)

        # Creating matrix p
        matrix_p = np.zeros((self.nday + 1, self.x), dtype=float)
        matrix_p[0, :] = self.pinit
        matrix_p[0, -1] = self.pfinal
        matrix_p[:, 0] = self.pinit
        matrix_p[:, -1] = self.pfinal

        for index_row, row in enumerate(matrix_p):
            if index_row == 0:
                continue
            list_of_pressure_n_min_1 = matrix_p[index_row-1, :]
            list_of_pressure_n_min_1_inside = (list_of_pressure_n_min_1[1:-1])*(-1)
            matrix_b = np.copy(list_of_pressure_n_min_1_inside)
            matrix_b[0] = (list_of_pressure_n_min_1_inside[0]) - (self.beta * self.pinit)
            matrix_b[-1] = (list_of_pressure_n_min_1_inside[-1]) - (self.beta * self.pfinal)
            matrix_p[index_row, 1:-1] = np.matmul(matrix_a_inverted, matrix_b)

        column = list(range(1, self.x + 1))
        rows = np.array(list(range(0, self.nday + 1)))
        days = rows * self.dt
        df_implicit = pd.DataFrame(data=matrix_p, columns=column)
        df_implicit.index = days

        return df_implicit

    def create_tridiagonal_matrix(self, size_of_a_matrix, value_for_diagonal, value_for_above_diagonal,
                                  value_for_below_diagonal):
        """
        Fucntion to creating the tridiagonal matrix.

        Parameters
        ----------
        size_of_a_matrix
        value_for_diagonal
        value_for_above_diagonal
        value_for_below_diagonal

        Returns
        -------

        """
        if size_of_a_matrix <= 3:
            # since size should be greater than 3
            print("Please enter the size that is greater than 3")
            exit()

        diagonal = []
        numbers1 = [[0 for j in range(0, size_of_a_matrix)]
                    for i in range(0, size_of_a_matrix)]

        # Created a loop to enter numbers of diagonal
        for a in range(size_of_a_matrix):
            numbers1 = value_for_diagonal
            diagonal.append(numbers1)

        # Created a loop to enter numbers of above diagonal
        diagonalAbove = []
        for k in range(size_of_a_matrix - 1):
            numbers2 = value_for_above_diagonal
            diagonalAbove.append(numbers2)

        # Created a loop to enter numbers of below diagonal
        diagonalBelow = []
        for z in range(size_of_a_matrix - 1):
            numbers3 = value_for_below_diagonal
            diagonalBelow.append(numbers3)

        matrix = [[0 for j in range(size_of_a_matrix)]
                  for i in range(size_of_a_matrix)]

        for k in range(size_of_a_matrix - 1):
            matrix[k][k] = diagonal[k]
            matrix[k][k + 1] = diagonalAbove[k]
            matrix[k + 1][k] = diagonalBelow[k]

        matrix[size_of_a_matrix - 1][size_of_a_matrix - 1] = diagonal[size_of_a_matrix - 1]

        return np.array(matrix)

    def plot(self, df, graph_title):
        fig = px.line(df, title=graph_title, labels={'index': 'Days', 'value': 'Pressure', 'variable': 'Blocks'})

        return fig.show()


if __name__ == "__main__":
    result_explicit = Simres().explicit()
    print('Explicit Solution')
    print(Simres().explicit())
    Simres().plot(df=result_explicit, graph_title='Explicit Solution')

    result_implicit = Simres().implicit()
    print('Implicit Solution')
    print(Simres().implicit())
    Simres().plot(df=result_implicit, graph_title='Implicit Solution')
