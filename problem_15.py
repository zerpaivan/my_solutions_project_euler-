# to create the grid
grid_i = 20
grid_j = 20
grid = []
row = [0] * (grid_j + 1)
grid.append(row[:])

for i in range(grid_i):
    grid.append(row[:])

# initial conditions grid r(0,n) = 1 and c(n, 0) = 1
for j in range(1, grid_j + 1):
    grid[0][j] = 1

for i in range(1, grid_i + 1):
    grid[i][0] = 1

# solve the rest of the nodes, adding adjacent nodes
for i in range(1, grid_i + 1):
    for j in range(1, grid_j + 1):
        grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

for n in grid:
    print(n)

print("\nsolution: ", grid[grid_i][grid_j])
