from io import StringIO
from unittest import main, TestCase
from Life import Life, AbstractCell, ConwayCell, FredkinCell, life_read

class TestLife(TestCase):
	# AC init
	def test_ACinit_1(self):
		cell = ConwayCell('*', 1, 5)
		self.assertEqual(cell.state, '*')
		self.assertEqual(cell.x, 1)
		self.assertEqual(cell.y, 5)

	def test_ACinit_2(self):
		cell = ConwayCell('.', 2, 3)
		self.assertEqual(cell.state, '.')
		self.assertEqual(cell.x, 2)
		self.assertEqual(cell.y, 3)

	def test_ACinit_3(self):
		cell = FredkinCell('-', 3, 9)
		self.assertEqual(cell.state, '-')
		self.assertEqual(cell.x, 3)
		self.assertEqual(cell.y, 9)

	# change state
	def test_change_state_1(self):
		cell = ConwayCell('*', 1, 5)
		cell.change_state()
		self.assertEqual(cell.future, '.')

	def test_change_state_2(self):
		cell = ConwayCell('.', 2, 3)
		cell.change_state()
		self.assertEqual(cell.future, '*')

	def test_change_state_3(self):
		cell = ConwayCell('.', 6, 5)
		cell.change_state()
		self.assertEqual(cell.future, '*')		

	def test_change_state_4(self):
		cell = FredkinCell('-', 3, 9)
		cell.change_state()
		self.assertEqual(cell.future, 0)

	def test_change_state_5(self):
		cell = FredkinCell('0', 5, 9)
		cell.change_state()
		self.assertEqual(cell.future, '-')

	def test_change_state_6(self):
		cell = FredkinCell('-', 6, 4)
		cell.change_state()
		self.assertEqual(cell.future, 0)

	# keep state rest
	def test_keep_state_reset_1(self):
		cell = ConwayCell('*', 1, 5)
		cell.future = '.'
		cell.count = 1
		cell.keep_state_reset()
		cell.state = '.'
		cell.count = 0

	def test_keep_state_reset_2(self):
		cell = ConwayCell('.', 3, 8)
		cell.future = '*'
		cell.count = 3
		cell.keep_state_reset()
		cell.state = '*'
		cell.count = 0

	def test_keep_state_reset_3(self):
		cell = FredkinCell('1', 0, 7)
		cell.future = '*'
		cell.count = 3
		cell.keep_state_reset()
		cell.state = '*'
		cell.count = 0

	# CC init
	def test_CCinit_1(self):
		cell = ConwayCell('.', 2, 3)
		self.assertEqual(cell.state, '.')
		self.assertEqual(cell.x, 2)
		self.assertEqual(cell.y, 3)
		self.assertEqual(cell.type_cell, 'Conway')

	def test_CCinit_2(self):
		cell = ConwayCell('*', 5, 3)
		self.assertEqual(cell.state, '*')
		self.assertEqual(cell.x, 5)
		self.assertEqual(cell.y, 3)
		self.assertEqual(cell.type_cell, 'Conway')

	def test_CCinit_3(self):
		cell = ConwayCell('.', 9, 3)
		self.assertEqual(cell.state, '.')
		self.assertEqual(cell.x, 9)
		self.assertEqual(cell.y, 3)
		self.assertEqual(cell.type_cell, 'Conway')

	# FC init
	def test_FCinit_1(self):
		cell = FredkinCell('-', 9, 3)
		self.assertEqual(cell.state, '-')
		self.assertEqual(cell.x, 9)
		self.assertEqual(cell.y, 3)
		self.assertEqual(cell.type_cell, 'Fredkin')

	def test_FCinit_2(self):
		cell = FredkinCell('0', 4, 5)
		self.assertEqual(cell.state, 0)
		self.assertEqual(cell.age, 0)
		self.assertEqual(cell.x, 4)
		self.assertEqual(cell.y, 5)
		self.assertEqual(cell.type_cell, 'Fredkin')

	def test_FCinit_3(self):
		cell = FredkinCell('-', 3, 4)
		self.assertEqual(cell.state, '-')
		self.assertEqual(cell.x, 3)
		self.assertEqual(cell.y, 4)
		self.assertEqual(cell.type_cell, 'Fredkin')

	# L init
	def test_Linit_1(self):
		x = Life(2, 15, [['.','.','*','.','.','.','.','.','*','.','.','.','.','.','.'], ['.','.','.','.','.','.','.','.','.','*','.','.','.','.','.']])
		self.assertEqual(x.row, 2)
		self.assertEqual(x.col, 15)
		self.assertEqual(x.population, 3)
		self.assertEqual(x.generation, 0)

	def test_Linit_2(self):
		x = Life(2, 2, [['.','.'], ['*','*']])
		self.assertEqual(x.row, 2)
		self.assertEqual(x.col, 2)
		self.assertEqual(x.population, 2)
		self.assertEqual(x.generation, 0)

	def test_Linit_3(self):
		x = Life(5, 3, [['.','.','.'], ['*','.','.'], ['*','*','*'], ['.','.','*'], ['.','.','*']])
		self.assertEqual(x.row, 5)
		self.assertEqual(x.col, 3)
		self.assertEqual(x.population, 6)
		self.assertEqual(x.generation, 0)

	# simulate
	def test_simulate_1(self):
		x = Life(2, 15, [['.','.','*','.','.','.','.','.','*','.','.','.','.','.','.'], ['.','.','.','.','.','.','.','.','.','*','.','.','.','.','.']])
		x.moat_grid()
		x.simulate()
		x.generation = 1

	def test_simulate_2(self):
		x = Life(2, 15, [['.','.','*','.','.','.','.','.','*','.','.','.','.','.','.'], ['.','.','.','.','.','.','.','.','.','*','.','.','.','.','.']])
		x.moat_grid()
		x.simulate()
		x.generation = 1

	def test_simulate_3(self):
		x = Life(2, 2, [['.','.'], ['*','*']])
		x.moat_grid()
		x.simulate()
		x.generation = 1

	# count pop
	def test_count_pop_1(self):
		x = Life(2, 15, [['.','.','*','.','.','.','.','.','*','.','.','.','.','.','.'], ['.','-','.','.','.','.','.','.','.','*','.','.','.','.','.']])
		x.moat_grid()
		x.count_pop()
		self.assertEqual(x.population, 3)

	def test_count_pop_2(self):
		x = Life(5, 3, [['.','.','.'], ['*','.','.'], ['*','*','*'], ['.','.','*'], ['.','.','*']])
		x.moat_grid()
		x.count_pop()
		self.assertEqual(x.population, 6)

	def test_count_pop_3(self):
		x = Life(3, 10, [['.','.','*','.','.','.','.','.','*','.'], ['.','.','.','.','.','.','.','.','.','*'], ['.','.','*','.','.','*','*','.','.','*']])
		x.moat_grid()
		x.count_pop()
		self.assertEqual(x.population, 7)
	
	# moat grid
	def test_moat_grid_1(self):
		x = Life(3, 10, [['.','.','*','.','.','.','.','.','*','.'], ['.','.','.','.','.','.','.','.','.','*'], ['.','.','*','.','.','*','*','.','.','*']])
		grid = len(x.grid)
		x.moat_grid()
		self.assertEqual(grid + 2, len(x.grid))

	def test_moat_grid_2(self):
		x = Life(5, 3, [['.','.','.'], ['*','.','.'], ['*','*','*'], ['.','.','*'], ['.','.','*']])
		grid = len(x.grid)
		x.moat_grid()
		self.assertEqual(grid + 2, len(x.grid))

	def test_moat_grid_3(self):
		x = Life(2, 2, [['.','.'], ['*','*']])
		grid = len(x.grid)
		x.moat_grid()
		self.assertEqual(grid + 2, len(x.grid))

	# fut curr
	def test_fut_curr_1(self):
		x = Life(5, 3, [['.','.','.'], ['*','.','.'], ['*','*','*'], ['.','.','*'], ['.','.','*']])
		x.future = '.'
		x.moat_grid()
		x.fut_curr()
		x.grid[5][3].count = 0
		x.grid[5][3].state = '.'

	def test_fut_curr_2(self):
		x = Life(5, 3, [['.','.','.'], ['*','.','.'], ['*','*','*'], ['.','.','*'], ['.','.','*']])
		x.future = '*'
		x.moat_grid()
		x.fut_curr()
		x.grid[2][2].count = 0
		x.grid[2][2].state = '*'\

	def test_fut_curr_3(self):
		x = Life(5, 3, [['-','-','-'], ['0','1','0'], ['0','-','-'], ['-','-','0'], ['*','0','-']])
		x.future = '-'
		x.moat_grid()
		x.fut_curr()
		x.grid[2][3].count = 0
		x.grid[2][3].state = '-'
	
	# is conway
	def test_is_conway_1(self):
		x = Life(5, 3, [['.','.','.'], ['*','.','.'], ['*','*','*'], ['.','.','*'], ['.','.','*']])
		x.moat_grid()
		x.grid[4][3].type_cell = 'Conway'
		self.assertEqual(True, x.is_conway(4, 3))

	def test_is_conway_2(self):
		x = Life(5, 3, [['.','.','.'], ['*','.','.'], ['*','*','*'], ['.','.','*'], ['.','.','*']])
		x.moat_grid()
		x.grid[2][3].type_cell = 'Conway'
		self.assertEqual(True, x.is_conway(2, 3))

	def test_is_conway_3(self):
		x = Life(5, 3, [['0','0','0'], ['*','-','-'], ['-','-','*'], ['-','-','*'], ['-','-','*']])
		x.moat_grid()
		x.grid[5][1].type_cell = 'Fredkin'
		self.assertEqual(False, x.is_conway(5, 1))

	def test_is_conway_4(self):
		x = Life(5, 3, [['0','0','0'], ['*','-','-'], ['-','-','*'], ['-','-','*'], ['-','-','*']])
		x.moat_grid()
		x.grid[1][3].type_cell = 'Fredkin'
		self.assertEqual(False, x.is_conway(1, 3))

	def test_is_conway_5(self):
		x = Life(5, 3, [['0','0','0'], ['*','-','-'], ['-','-','*'], ['-','-','*'], ['-','-','*']])
		x.moat_grid()
		x.grid[2][3].type_cell = 'Fredkin'
		self.assertEqual(False, x.is_conway(2, 3))

	def test_is_conway_6(self):
		x = Life(5, 3, [['0','0','0'], ['*','-','-'], ['-','-','*'], ['-','-','*'], ['-','-','*']])
		x.moat_grid()
		x.grid[0][0].type_cell = 'Conway'
		self.assertEqual(True, x.is_conway(0, 0))

	# is self
	def test_is_self_1(self):
		x = Life(5, 3, [['.','*','.'], ['.','.','.'], ['*','.','*'], ['*','.','*'], ['.','.','*']])
		x.moat_grid()
		row = 3
		col = 3
		self.assertEqual(True, x.is_self(row, col, 3, 3))

	def test_is_self_2(self):
		x = Life(5, 3, [['.','*','.'], ['.','.','.'], ['*','.','*'], ['*','.','*'], ['.','.','*']])
		x.moat_grid()
		row = 1
		col = 4
		self.assertEqual(False, x.is_self(row, col, 1, 1))

	def test_is_self_3(self):
		x = Life(5, 3, [['.','*','.'], ['.','.','.'], ['*','.','*'], ['*','.','*'], ['.','.','*']])
		x.moat_grid()
		row = 2
		col = 4
		self.assertEqual(True, x.is_self(row, col, 2, 4))	

	# count (row + 1)
	def test_count_1(self):
		x = Life(5, 3, [['-','-','-'], ['0','1','0'], ['0','-','-'], ['-','-','0'], ['*','0','-']])
		x.moat_grid()
		x.count()
		self.assertEqual(x.grid[2][2].count, 2)
	
	def test_count_2(self):
		x = Life(5, 3, [['-','-','-'], ['0','1','0'], ['0','-','-'], ['-','-','0'], ['*','0','-']])
		x.moat_grid()
		x.count()
		self.assertEqual(x.grid[2][1].count, 2)
	
	def test_count_3(self):
		x = Life(5, 3, [['-','-','-'], ['0','1','0'], ['0','-','-'], ['-','-','0'], ['*','0','-']])
		x.moat_grid()		
		x.count()
		self.assertEqual(x.grid[5][1].count, 1)

	def test_count_4(self):
		x = Life(5, 3, [['.','*','.'], ['.','.','.'], ['*','.','*'], ['*','.','*'], ['.','.','*']])
		x.moat_grid()
		x.count()
		self.assertEqual(x.grid[4][1].count, 1)

	def test_count_5(self):
		x = Life(5, 3, [['.','*','.'], ['.','.','.'], ['*','.','*'], ['*','.','*'], ['.','.','*']])
		x.moat_grid()
		x.count()
		self.assertEqual(x.grid[1][2].count, 0)

	def test_count_6(self):
		x = Life(5, 3, [['-','-','-'], ['-','-','-'], ['0','-','-'], ['-','-','0'], ['*','0','-']])
		x.moat_grid()
		x.count()
		self.assertEqual(x.grid[5][2].count, 1)
	
	# future
	def test_future_1(self):
		x = Life(5, 3, [['-','0','-'], ['-','-','-'], ['-','-','-'], ['-','-','-'], ['-','-','-']])
		x.moat_grid()
		x.count()
		x.future()
		self.assertEqual(x.grid[1][2].state, 0)

	def test_future_2(self):
		x = Life(5, 3, [['.','*','.'], ['.','.','.'], ['*','.','*'], ['*','.','*'], ['.','.','*']])
		x.moat_grid()
		x.count()
		x.future()
		self.assertEqual(x.grid[3][3].state, '*')
	
	def test_future_3(self):
		x = Life(5, 3, [['.','*','.'], ['.','.','.'], ['*','.','*'], ['*','*','*'], ['.','.','*']])
		x.moat_grid()
		x.count()
		x.future()
		self.assertEqual(x.grid[2][3].state, '.')

	def test_future_4(self):
		x = Life(5, 3, [['-','0','-'], ['-','-','-'], ['-','-','-'], ['-','-','-'], ['-','-','-']])
		x.moat_grid()
		x.count()
		x.future()
		self.assertEqual(x.grid[2][2].state, '-')

	def test_future_5(self):
		x = Life(5, 3, [['.','*','.'], ['.','.','.'], ['*','.','*'], ['*','*','.'], ['.','.','*']])
		x.moat_grid()
		x.count()
		x.future()
		self.assertEqual(x.grid[4][3].state, '*')

	# life read
	def test_life_read_1(self):
		r = StringIO("2\n5\n.....\n*....\n")
		row, col, grid = life_read(r)
		self.assertEqual(row, 2)
		self.assertEqual(col, 5)

	def test_life_read_2(self):
		r = StringIO("5\n10\n..........\n....**...*\n")
		row, col, grid = life_read(r)
		self.assertEqual(row, 5)
		self.assertEqual(col, 10)

	def test_life_read_3(self):
		r = StringIO("25\n7\n.......\n..***..\n")
		row, col, grid = life_read(r)
		self.assertEqual(row, 25)
		self.assertEqual(col, 7)

	def test_life_read_4(self):
		r = StringIO("10\n2\n.......\n..***..\n")
		row, col, grid = life_read(r)
		self.assertEqual(row, 10)
		self.assertEqual(col, 2)
	
main()

# coverage3 run --branch TestLife.py > TestLife.out
# coverage3 report -m >> TestLife.out
# cat TestLife.out
