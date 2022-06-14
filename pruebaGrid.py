from grid import Grid
from cube import Cube

def main():
    rows = int(input("Digite las filas: "))
    col = int(input("Digite las Columnas: "))
    grid = Grid(rows, col)
    print(grid)
    grid.__setRandom__()
    print(grid)

    rows = int(input("Digite las filas del cubo: "))
    col = int(input("Digite las Columnas del cubo: "))
    dep = int(input("Digite la Profundidad del cubo: "))
    cube = Cube(rows, col, dep)
    print(cube)

if __name__ == '__main__':
    main()