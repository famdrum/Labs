import shutil
import zipfile
from pathlib import Path

class ZipProcessor:
	def __init__(self, zipname):
		"""
		Sets the value of zipname and temp_directory
		"""
		self.zipname = zipname
		self.temp_directory = Path("unzipped-{}".format(zipname[:-4]))
	
	def process_zip(self):
		"""
		Calls unzip_files, process_filesa and zip_files functions
		"""
		self.unzip_files()
		self.process_files()
		self.zip_files()
	
	def unzip_files(self):
		"""
		Makes a new directory and extracts all members of the zip to it.
		"""
		self.temp_directory.mkdir()
		with zipfile.ZipFile(self.zipname) as zip:
			zip.extractall(str(self.temp_directory))
	
	def zip_files(self):
		"""
		Rewrites a zip and deletes a directory
		"""
		with zipfile.ZipFile(self.zipname, 'w') as file:
			for filename in self.temp_directory.iterdir():
				file.write(str(filename), filename.name)
		shutil.rmtree(str(self.temp_directory))
