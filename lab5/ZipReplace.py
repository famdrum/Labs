from ZipProcessor import ZipProcessor

class ZipReplace():
	def __init__(self, filename, search_string,replace_string):
		"""
		Creates initial variables
		"""
		self.var = ZipProcessor(filename)
		self.search_string = search_string
		self.replace_string = replace_string
	def process_files(self):
		'''perform a search and replace on all files
		in the temporary directory'''
		for filename in self.var.temp_directory.iterdir():
			with filename.open() as file:
				contents = file.read()
			contents = contents.replace(self.search_string, self.replace_string)
			with filename.open("w") as file:
				file.write(contents)
	def process_zip(self):
		"""
		Calls functions from ZipProcessor for work
		"""
		self.var.unzip_files()
		self.process_files()
		self.var.zip_files()
