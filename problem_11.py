from math import prod
grid_path = "20x20_grid.txt"


def load_grid(grid_path):  # function for load the grid
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
    max_product = 0

# ---------------------------------------
# to move the node grid[n][m] right, down, and right-diagonals

    for n in range(len_rows):
        for m in range(len_columns):
            H = []
            V = []
            D1 = []
            D2 = []

            for e in range(n_elements):
                if m + n_elements <= len_columns:
                    H.append(int(grid[n][m + e]))
                if n + n_elements <= len_rows:
                    V.append(int(grid[n + e][m]))
                if n + n_elements <= len_rows and m + n_elements <= len_columns:
                    D1.append(int(grid[n + e][m + e]))
                if n - n_elements > 0 and m + n_elements <= len_columns:
                    D2.append(int(grid[n - e][m + e]))

            partial_sol = [H, V, D1, D2]
            def check_product(x): return prod(x) > max_product

            for i in partial_sol:
                if check_product(i):
                    max_product = prod(i)
                    numbers = i
                    node = (n, m)

    print("product: ", max_product, "numbers: ", numbers, "node: ", node)


grid_n = load_grid(grid_path)
largest_product(4, grid_n)
