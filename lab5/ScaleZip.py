from ZipProcessor import ZipProcessor
import os
import sys
from pygame import image
from pygame.transform import scale

class ScaleZip():
	def __init__(self, filename):
		"""
		Creates a ZipProcessor object
		"""
		self.var = ZipProcessor(filename)
	def process_files(self, x, y):
		'''
		Scales each image in the directory to some size
		'''
		self.var.unzip_files()
		for filename in self.var.temp_directory.iterdir():
			im = image.load(str(filename))
			scaled = scale(im, (int(x), int(y)))
			image.save(scaled, filename)
		self.var.zip_files()
