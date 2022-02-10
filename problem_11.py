grid_path = "20x20_grid.txt"


def load_grid(grid_path):
    file_grid = open(grid_path, 'r')
    grid = []

    for n in file_grid:
        grid.append(n.rstrip().split(' '))

    file_grid.close()
    return grid

grid_n = load_grid(grid_path)
print(grid_n)
# grip = file_grip.readlines()
# print(grip)
