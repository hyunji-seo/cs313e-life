from io import StringIO
from unittest import main, TestCase
from Life import Life, AbstractCell, ConwayCell, FredkinCell, life_read

class TestLife (TestCase):
	
	# change state
	def change_state_1(self):
		cell = ConwayCell('*', 1, 5)
		cell.change_state('Conway')
		self.assertEqual(cell.future, '.')

	def change_state_2(self):
		cell = ConwayCell('.', 2, 3)
		cell.change_state('Conway')
		self.assertEqual(cell.future, '*')

	def change_state_3(self):
		cell = FredkinCell('-', 3, 9)
		cell.change_state('Fredkin')
		self.assertEqual(cell.future, 0)

	def change_state_4(self):
		cell = FredkinCell('0', 5, 9)
		cell.change_state('Fredkin')
		self.assertEqual(cell.future, '-')

	def change_state_5(self):
		cell = FredkinCell('-', 6, 4)
		cell.change_state('Fredkin')
		self.assertEqual(cell.future, 1)

	# keep state rest
	def keep_state_reset_1(self):
		cell = ConwayCell('*', 1, 5)
		cell.future = '.'
		cell.count = 1
		cell.keep_state_reset()
		cell.state = '.'
		cell.count = 0

	def keep_state_reset_2(self):
		cell = ConwayCell('.', 3, 8)
		cell.future = '*'
		cell.count = 3
		cell.keep_state_reset()
		cell.state = '*'
		cell.count = 0

	def keep_state_reset_3(self):
		cell = FredkinCell('1', 0, 7)
		cell.future = '*'
		cell.count = 3
		cell.keep_state_reset()
		cell.state = '*'
		cell.count = 0

	# print grid
		
	def simulate(self):
		x = Life(2, 15, ['..*.....*......', '.........*.....'])
		x.simulate()
		x.generation = 1

	# count pop
	def count_pop_1(self):
		x = Life(2, 15, ['..*.....*......', '.........*.....'])
		x.count_pop()
		self.assertEqual(x.population, 3)

	def count_pop_2(self):
		x = Life(5, 3, ['..., *.., ***, ..*, ..*'])
		x.count_pop()
		self.assertEqual(x.population, 6)

	def count_pop_3(self):
		x = Life(3, 10, ['..*.....*.', '.........*, ..*..**..*'])
		x.count_pop()
		self.assertEqual(x.population, 7)
	
	# moat grid
	def moat_grid_1(self):
		x = Life(3, 10, ['..*.....*.', '.........*, ..*..**..*'])
		grid = len(x.grid)
		x.moat_grid()
		self.assertEqual(grid + 2, len(x.grid))

	def moat_grid_2(self):
		x = Life(5, 3, ['..., *.., ***, ..*, ..*'])
		grid = len(x.grid)
		x.moat_grid()
		self.assertEqual(grid + 2, len(x.grid))

	def moat_grid_3(self):
		x = Life(2, 2, ['.., **'])
		grid = len(x.grid)
		x.moat_grid()
		self.assertEqual(grid + 2, len(x.grid))

	# fut curr
	def fut_curr_1(self):
		x = Life(5, 3, ['..., *.., ***, ..*, ..*'])
		x.future = '.'
		x.fut_curr()
		x.grid[5][3].count = 0
		x.grid[5][3].state = '.'

	def fut_curr_2(self):
		x = Life(5, 3, ['..., *.., ***, ..*, ..*'])
		x.future = '*'
		x.fut_curr()
		x.grid[2][2].count = 0
		x.grid[2][2].state = '*'\

	def fut_curr_3(self):
		x = Life(5, 3, ['---, 010, 0--, --0, *0-'])
		x.future = '-'
		x.fut_curr()
		x.grid[2][3].count = 0
		x.grid[2][3].state = '-'
	
	# is conway
	def is_conway_1(self):
		x = Life(5, 3, ['..., *.., ***, ..*, ..*'])
		x.grid[4][3].type_cell = 'Conway'
		self.assertEqual(True, is_conway(4, 3))

	def is_conway_2(self):
		x = Life(5, 3, ['.*., ..., *.*, *.*, ..*'])
		x.grid[2][3].type_cell = 'Conway'
		self.assertEqual(True, is_conway(2, 3))

	def is_conway_3(self):
		x = Life(5, 3, ['101, *--, --*, --*, --*'])
		x.grid[5][1].type_cell = 'Fredkin'
		self.assertEqual(False, is_conway(5, 1))

	def is_conway_4(self):
		x = Life(5, 3, ['101, *--, --*, --*, --*'])
		x.grid[1][3].type_cell = 'Fredkin'
		self.assertEqual(False, is_conway(1, 3))

	# is self
	def is_self_1(self):
		x = Life(5, 3, ['.*., ..., *.*, *.*, ..*'])
		row = 3
		col = 3
		self.assertEqual(True, x.is_self(row, col, 3, 3))

	def is_self_2(self):
		x = Life(5, 3, ['.*., ..., *.*, *.*, ..*'])
		row = 1
		col = 4
		self.assertEqual(False, x.is_self(row, col, 1, 1))		

	# life read
	def life_read_1(self):
		r = StringIO("2\n5\n.....\n*....\n")
		row, col, grid = life_read(r)
		self.assertEqual(row, 2)
		self.assertEqual(col, 5)

	def life_read_2(self):
		r = StringIO("5\n10\n..........\n....**...*\n")
		row, col, grid = life_read(r)
		self.assertEqual(row, 5)
		self.assertEqual(col, 10)

	def life_read_3(self):
		r = StringIO("25\n7\n.......\n..***..\n")
		row, col, grid = life_read(r)
		self.assertEqual(row, 25)
		self.assertEqual(col, 7)
	
main()

# coverage3 run --branch TestLife.py > TestLife.out 2>&1
# coverage3 report -m >> TestLife.out
# cat TestLife.out
