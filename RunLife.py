# -------
# imports
# -------

import sys
from Life import Life, AbstractCell, ConwayCell, FredkinCell, life_read

# ---------------------
# Life ConwayCell 21x13
# ---------------------

print("*** Life ConwayCell 21x13 ***")
"""
Simulate 12 evolutions.
Print every grid (i.e. 0, 1, 2, 3, ... 12)
"""
row, col, grid = life_read(sys.stdin)
x = Life(row, col, grid)
x.moat_grid()
x.print_grid(12, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# ---------------------
# Life ConwayCell 20x29
# ---------------------

print("*** Life ConwayCell 20x29 ***")
"""
Simulate 28 evolutions.
Print every 4th grid (i.e. 0, 4, 8, ... 28)
"""
row, col, grid = life_read(sys.stdin)
x = Life(row, col, grid)
x.moat_grid()
x.print_grid(28,[4,8,12,16,18,20,24,28])

# ----------------------
# Life ConwayCell 109x69
# ----------------------

print("*** Life ConwayCell 109x69 ***")
"""
Simulate 283 evolutions.
Print the first 10 grids (i.e. 0, 1, 2, ... 9).
Print the 283rd grid.
Simulate 40 evolutions.
Print the 323rd grid.
Simulate 2177 evolutions.
Print the 2500th grid.
"""
row, col, grid = life_read(sys.stdin)
x = Life(row, col, grid)
x.moat_grid()
x.print_grid(2500, [1,2,3,4,5,6,7,8,9,283,323,2499,2500])

# ----------------------
# Life FredkinCell 20x20
# ----------------------

print("*** Life FredkinCell 20x20 ****")
"""
Simulate 5 evolutions.
Print every grid (i.e. 0, 1, 2, ... 5)
"""
row,col,grid = life_read(sys.stdin)
x = Life(row, col, grid)
x.moat_grid()
x.print_grid(5, [1,2,3,4,5])
