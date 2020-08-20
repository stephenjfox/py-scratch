from grid import Grid, grid_cells

if __name__ == "__main__":
    grid = Grid(rows=[grid_cells(1), grid_cells(3)])
    print(grid.dimensions)
    print(grid)

    grid.insert_column(at=2)

    print("New dimensions:", grid.dimensions)
    print(grid)
    # TODO
    # grid.grow(axis='column')
    # grid.grow(axis='row')
    grid.grow(axis='row')
    print("New dimensions:", grid.dimensions)
    print(grid)

    grid.grow(axis='column')
    print("New dimensions:", grid.dimensions)
    print(grid)