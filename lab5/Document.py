from Cursor import Cursor
from Character import Character

class NoName(Exception):
	def message(self):
		"""
		Prints a warning message
		"""
		print('You did not enter a name of file.')

class TooMuch(Exception):
	def message(self):
		"""
		Prints a warning message
		"""
		print('Only one letter is allowed.')

class NotFound(Exception):
	def message(self):
		"""
		Prints a warning message
		"""
		print('There is no such character in list')

class Document:
	def __init__(self, filename=''):
		"""
		Creates initial variables
		"""
		self.characters = []
		self.cursor = Cursor(self)
		self.filename = filename
	def insert(self, character):
		"""
		Inserts a new character
		"""
		try:
			if type(character) == str:
				if len(character) > 1:
					raise TooMuch
				else:
					self.characters.insert(self.cursor.position,character)
					self.cursor.forward()
			else:
				self.characters.insert(self.cursor.position,character)
				self.cursor.forward()
				
		except TooMuch as error:
			error.message()
	def delete(self):
		"""
		Deletes a character with current position
		"""
		try:
			if len(self.characters) != 0 and not (self.cursor.position > len(self.characters)):
				del self.characters[self.cursor.position - 1]
			else:
				raise NotFound
		except NotFound as error:
			error.message()
	def save(self):
		"""
		Saves progress in file
		"""
		try:
			if self.filename == '':
				raise NoName
			else:
				f = open(self.filename, 'w')
				f.write(''.join(self.characters))
				f.close()
		except NoName as error:
			error.message()
	@property
	def string(self):
		"""
		Joins all characters into one string and prints it
		"""
		return "".join((str(c) for c in self.characters))
