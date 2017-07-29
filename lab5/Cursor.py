class BadMovement(Exception):
	def message_f(self):
		"""
		Prints a warning message
		"""
		print("Entered position is too big.")
	def message_b(self):
		"""
		Prints a warning message
		"""
		print("Entered position is too small.")

class Cursor:
	def __init__(self, document):
		"""
		Creates initial variables
		"""
		self.document = document
		self.position = 0
	def forward(self):
		"""
		Adds one point to character's position
		"""
		try:
			if self.position == len(self.document.characters):
				raise BadMovement
			else:
				self.position += 1
		except BadMovement as error:
			error.message_f()
	def back(self):
		"""
		Substracts one point from character's position
		"""
		try:
			if self.position == 0:
				raise BadMovement
			else:
				self.position -= 1
		except BadMovement as error:
			error.message_b()
	def home(self):
		"""
		Sets the initial position
		"""
		while self.document.characters[self.position-1] != '\n':
			self.position -= 1
			if self.position == 0:
				# Got to beginning of file before newline
				break
	def end(self):
		"""
		Sets the last position
		"""
		while self.position < len(self.document.characters) and self.document.characters[self.position] != '\n':
			self.position += 1
