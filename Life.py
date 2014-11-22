# -----------------
# Life.py
# Copyright 2014
# Sanghyeok Park
# Hyunji Seo
# -----------------

# ------------------
# Class AbstractCell
# ------------------

class AbstractCell :
	"""
	__init__ Initializes both type of cells
	change_State changes the cell between dead/alive
	keep_state_reset pushes future to current and resets count
	"""
	def __init__(self, state, x, y):
		self.state = state
		self.x = x
		self.y = y
		self.future = ""
		self.count = 0

	def change_state (self, type_cell):
		if self.type_cell == 'Conway':
		  if self.state == "*":
		      self.future = "."
		  elif self.state == '.':
			  self.future = "*"
		if type_cell == 'Fredkin':
			if self.state == '-':
				try:
					self.future = self.age
				except AttributeError:
					self.future = 0
					self.age = 0
			else:
				self.future = '-'

	def keep_state_reset (self) :
		self.state = self.future
		self.count = 0

# ------------------
# Class ConwayCell
# ------------------

class ConwayCell (AbstractCell) :
	"""
	Initializes a ConwayCell when called
	Inherits Parent class AbstractCell
	"""
	def __init__(self, state, x, y):
		AbstractCell.__init__(self, state, x, y)
		self.type_cell = 'Conway'	

	def change_state(self):
		AbstractCell.change_state(self, self.type_cell)

# ------------------
# Class FredkinCell
# ------------------

class FredkinCell (AbstractCell) :
	"""
	Initializes a FredkinCell
	Inherits Parent Class AbstractCell
	"""
	def __init__(self, state, x, y):
		if state == "0":
			self.state = 0
			self.age = 0
		else:
			self.state = state
		AbstractCell.__init__(self, self.state, x, y)
		self.type_cell = 'Fredkin'

	def change_state(self):
		AbstractCell.change_state(self, self.type_cell)

# ------------------
# Class Life
# ------------------

class Life :
	"""
	__init__ creates the grid
	print_grid prints the grid
	simulate simulates the evolution
	count_pop counts population
	moat_grid creates moat
	fut_curr changes the future and current values
	is_conway checks for conway cells
	is_self checks if it is itself
	count counts neighboring live cells
	future replaces the future values
	"""
	def __init__(self, row, col, grid) :
		self.row = row
		self.col = col
		self.population = 0
		self.grid = []
		for r in range(self.row):
			self.temp = []
			for c in range(self.col):
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
				print(cell.state, end='')
			print()

		for i in range(1, simulation + 1):
			self.simulate()
			if self.generation in evolution:
				print()
				print("Generation =", str(self.generation) + ",", "Population =", str(self.population) + ".")
				for r in range(1, self.row + 1):
					for c in range(1, self.col + 1):
						cell = self.grid[r][c]
						print(cell.state, end='')
					print()
		print()

	def simulate(self):
		self.count()
		self.future()
		self.fut_curr()
		self.count_pop()
		self.generation += 1

	def count_pop(self):
		self.population = 0
		for r in range(1, self.row):
			for c in range(1, self.col):
				cell = self.grid[r][c]
				if cell.state == '*' or type(cell.state) is int:
					self.population += 1

	def moat_grid(self):
		moat = []
		for j in range(self.row):
			self.grid[j].insert(0, ConwayCell('.', j, 0))
			self.grid[j].insert(self.col+1, ConwayCell('.', j, 0))
		for i in range(self.col):
			moat.insert(0,ConwayCell('.', 0, 0))
		self.grid = [moat] + self.grid
		self.grid = self.grid + [moat]

	def fut_curr(self):
		for r in range(1, self.row + 1):
			for c in range(1, self.col + 1):
				cell = self.grid[r][c]
				cell.keep_state_reset()

	def is_conway(self, r, c):
		if self.grid[r][c].type_cell == "Conway":
			return True
		return False

	def is_self(self, row, col, r, c):
		if self.grid[row][col] is self.grid[r][c]:
			return True
		return False

	def count(self):
		for r in range(self.row):
			for c in range(self.col):
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
							if self.grid[row][col].type_cell == "Fredkin":	
								if (row == r or col == c):
									if self.is_self(row,col,r,c) == False:
										self.grid[row][col].count += 1
									else:
										pass
	def future(self):
		for r in range(1, self.row + 1):
			for c in range(1, self.col + 1):
				cell = self.grid[r][c]
				if cell.state == '*':
					if cell.count < 2 or cell.count > 3:
						cell.change_state()
					else:
						cell.future = '*'
				elif cell.type_cell == "Fredkin" and cell.state != '-':
					if cell.count == 0 or cell.count == 2 or cell.count == 4:
						cell.change_state()
					else:
						if cell.age == 1:
							cell = ConwayCell('*', r - 1, c - 1)
						elif cell.age < 1:
							cell.age += 1
							cell.future = cell.age
				elif cell.state == '.':
					if cell.count == 3:
						cell.change_state()
					else:
						cell.future = '.'
				elif cell.state == '-':
					if cell.count == 1 or cell.count == 3:
						cell.change_state()
					else:
						cell.future = '-'
# ------------------
# Read Function
# ------------------

def life_read(r):
	"""
	r is a reader
	Reads the test cases
	"""
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
	r.readline()
	return row, col, grid
