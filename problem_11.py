grid_path = "20x20_grid.txt"


def load_grid(grid_path):
    file_grid = open(grid_path, 'r')
    grid = []

    for n in file_grid:
        grid.append(n.rstrip().split(' '))

    file_grid.close()
    return grid


def largest_product(n_elements, grid):
    len_rows = len(grid)
    len_columns = len(grid[0])
    print(len_rows, len_columns)
    for n in range(len_rows):
        for m in range(len_columns):
            H = []
            V = []
            if m + n_elements <= len_columns:
                for e in range(n_elements):
                    H.append(grid[n][m + e])
                print("H", H)
            if n + n_elements <= len_rows:
                for e in range(n_elements):
                    V.append(grid[n + e][m])
                print("V", V)




grid_n = load_grid(grid_path)
largest_product(4, grid_n)
