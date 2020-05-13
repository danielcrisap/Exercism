class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = [
            [int(item) for item in col.split(" ")] for col in matrix_string.split("\n")
        ]

    def row(self, index):
        return self.matrix_string[index - 1]

    def column(self, index):
        return [i[index - 1] for i in self.matrix_string]
