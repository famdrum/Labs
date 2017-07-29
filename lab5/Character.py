class TooMuch(Exception):
	def message(self):
		"""
		Prints a warning message
		"""
		print('Only one letter is allowed.')

class Character:
	def __init__(self, character,bold=False, italic=False, underline=False):
		"""
		Creates initial variables
		"""
		self.check = ''
		try:
			if len(character) > 1:
				self.check = 'no'
				raise TooMuch
			else:
				assert len(character) == 1
				self.character = character
				self.bold = bold
				self.italic = italic
				self.underline = underline
		except TooMuch as error:
			error.message()
	def __str__(self):
		"""
		Sets a type of character
		"""
		if not self.check == 'no':
			bold = "*" if self.bold else ''
			italic = "/" if self.italic else ''
			underline = "_" if self.underline else ''
			return bold + italic + underline + self.character
		else:
			return ''
