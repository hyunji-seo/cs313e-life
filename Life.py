class AbstractCell :
	def __init__(self, state, x, y):
		self.state = state
		self.x = x
		self.y = y
		self.future = ""
		self.count = 0

	def change_state (self, type_cell):
		if type_cell == 'Conway':
		  if self.state == "*":
		      self.future = "."
		  else:
			  self.future = "*"
		if type_cell == 'Fredkin':
			if self.state == '-':
				self.future = self.age
			else:
				self.future = '-'

	def keep_state_reset (self) :
		self.state = self.future
		self.count = 0

class ConwayCell (AbstractCell) :
	def __init__(self, state, x, y):
		AbstractCell.__init__(self, state, x, y)
		self.type_cell = 'Conway'	

	def change_state(self):
		AbstractCell.change_state(self, self.type_cell)


class FredkinCell (AbstractCell) :
	def __init__(self, state, x, y):
		self.age = state
		AbstractCell.__init__(self, self.age, x, y)
		self.type_cell = 'Fredkin'

	def change_state(self):
		AbstractCell.change_state(self, self.type_cell)

class Life :
	def __init__(self, row, col, grid) :
		self.row = row
		self.col = col
		self.population = 0
		self.grid = []
		self.temp = []
		for r in range(self.row-1):
			self.grid = []
			for c in range(self.col-1):
				if grid[r][c] == '.':
					self.temp.append(ConwayCell('.', r, c))
				elif grid[r][c] == '*':
					self.temp.append(ConwayCell('*', r, c))
					self.population += 1
				elif grid[r][c] == '0':
					self.temp.append(FredkinCell(0, r, c))
					self.population += 1
				elif grid[r][c] == '-':
					self.temp.append(FredkinCell('-', r, c))
				self.grid.append(self.temp)
		self.generation = 0

	def print_grid(self, simulation, evolution):
		print()
		print("Generation =", str(self.generation) + ",", "Population =", str(self.population) + ".")
		for r in range(1, self.row + 1):
			for c in range(1, self.col + 1):
				cell = self.grid[r][c]
				print(cell.current, end='')
			print()

		for i in range(1, simulation):
			self.simulate()
			if self.generation in evolution:
				for r in range(1, self.row + 1):
					for c in range(1, self.col + 1):
						cell = self.grid[r][c]
						print(cell.current, end='')
					print()


	def simulate(self):
		self.count()
		self.future()
		self.fut_curr()
		self.generation += 1

	def count_pop(self):
		for r in range(1, self.row):
			for c in range(1, self.col):
				cell = self.grid[r][c]
				if cell.state == '*' or type(cell.state) is int:
					self.population += 1

	def moat_grid(self):
		moat = []
	#	print(self.row, self.col)
		for j in range(self.row-1):
			print(len(self.grid))
			self.grid[j].insert(0, ConwayCell('.', j, 0))
			self.grid[j].insert(self.col, ConwayCell('.', j, 0))
		for i in range(len(self.grid[0])):
			moat.append([ConwayCell('.', 0, 0)])
		self.grid = moat + self.grid
		self.grid = self.grid + moat

	def fut_curr(self):
		for r in range(1, self.row + 1):
			for c in range(1, self.col + 1):
				cell = self.grid[r][c]
				cell.AbstractCell.keep_state_reset()

	def is_conway(self, r, c):
		if self.grid[r][c].cell_type == "Conway":
			return True
		return False

	def is_self(self, row, col, r, c):
		if self.grid[row][col] is self.grid[r][c]:
			return True
		return False

	def count(self):
		for r in self.row:
			for c in self.col:
				cell = self.grid[r][c]
				if cell.state == '*' or type(cell.state) is int:
					for row in range(r - 1, r + 2):
						for col in range(c - 1, c + 2):
							if col != c or row != r:
								if self.is_conway(row,col) == True:
									self.grid[row][col].count += 1
								else:
									pass
							elif self.is_self(row,col,r,c):
								pass
							else:
								self.grid[row][col].count += 1

	def future(self):
		for r in range(1, self.row + 1):
			for c in range(1, self.col + 1):
				cell = self.grid[r][c]
				if cell.state == '*':
					if cell.count != 2 or cell.count != 3:
						cell.change_state()
				if type(self.grid[r][c].state) is int:
					if cell.count == 0:
						cell.change_state()
					elif cell.count % 2:
						cell.change_state()
					else:
						if cell.age == 1:
							cell = ConwayCell('*', r - 1, c - 1)
						else:
							cell.age += 1
				if cell.state == '.':
					if cell.count == 3:
						cell.change_state()
				if cell.state == '-':
					if cell.count % 2 != 0:
						cell.change_state()






def life_read(r):
	grid = list()
	row = int(r.readline())
	col = int(r.readline())
	counter = 0
	while counter != row:
		line = r.readline()
		line = line.strip()
		line = line.replace("\n", '')
		line = list(line)
		grid.append(line)
		counter += 1
	print(grid)
	return row, col, grid








# identify neighbors
# retain age for Fredkins
