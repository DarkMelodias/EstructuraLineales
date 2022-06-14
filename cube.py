from my_array import Array


class Cube(object):
    """Represents a two-dimensional array."""
    def __init__(self, rows, columns, depth, fill_value = None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, fill_value)
            for column in range(columns):
                self.data[row][column] = Array(depth, fill_value)

    def get_height(self):
        "Returns the number of rows."
        return len(self.data)

    def get_width(self):
        """Returns the number of columns."""
        return len(self.data[0])
    
    def get_depth(self):
        """Returns the number of columns."""
        return len(self.data[0][0])


    def __getitem__(self, index):
        """Supports two-dimensional indexing with [row][column]."""
        return self.data[index]

    def __str__(self):
        """Returns a string representation of the grid."""
        result = ""

        for row in range(self.get_height()):
            for col in range(self.get_width()):
                for depth in range(self.get_depth()):
                    result += str(self.data[row][col][depth]) + " "

                result += "\n"

        return str(result)