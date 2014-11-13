class AbstractCell :
	def __init__(self, state, x, y):
		self.state = state
		self.x = x
		self.y = y
		self.future = ""

	def change_state (self):
		if self.state == "alive":
			self.future= "dead"
		else:
			self.future = "alive"

	def keep_state (self) :
		self.future = self.state

class ConwayCell (AbstractCell) :
	def __init__(self, state, x, y):
		AbstractCell.__init__(self, state, x, y)		

class FredkinCell (AbstractCell) :
	def __init__(self, state, x, y):
		AbstractCell.__init__(self, state, x, y)
		self.age = 0

class Life :
	def __init__(self, row, col) :
		self.row = row
		self.col = col
		self.generation = 0
		self.population = 0

	def print_grid(self):
		# print future state

	def count_grid(self):

	def grid(self):

def life_read(r):
	grid = deque()
	row = r.readline()
	col = r.readline()
	for i in range(int(row)):
		line = line.strip()
		line = line.split("")
		line = deque(line)
		grid.append(line)
	r.readline()
	return grid








# identify neighbors
# retain age for Fredkins
