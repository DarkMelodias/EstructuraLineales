"""
Code used for the 'Crear un array de dos dimensiones' class.

Grid type class
Methods:
    1. Initialize
    2. Get height
    3. Get width
    4. Access item
    5. String representation
"""
from my_array import Array
import random

class Grid(object):
    """Represents a two-dimensional array."""
    def __init__(self, rows, columns, fill_value = None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, fill_value)

    def get_height(self):
        "Returns the number of rows."
        return len(self.data)

    def get_width(self):
        """Returns the number of columns."""
        return len(self.data[0])

    def __getitem__(self, index):
        """Supports two-dimensional indexing with [row][column]."""
        return self.data[index]

    def __str__(self):
        """Returns a string representation of the grid."""
        result = ""

        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result += str(self.data[row][col]) + " "

            result += "\n"

        return str(result)

    def __setRandom__(self):
        """Returns a string representation of the grid."""
        result = 0
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                self.data[row][col] = random.randint(0, 100)
