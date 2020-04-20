class Matrix:
    def __init__(self, matrix_string):
        matrix_string = matrix_string.split("\n")
        matrix_col = []
        for item in matrix_string:
            matrix_row = []
            for element in item.split(" "):
                matrix_row.append(int(element))
            matrix_col.append(matrix_row)
        matrix = matrix_col
        self.matrix_string = matrix

    def row(self, index):
        matrix = self.matrix_string
        return matrix[index - 1]

    def column(self, index):
        matrix = self.matrix_string
        col = []
        for row in matrix:
            col.append(row[index-1])
        return col
