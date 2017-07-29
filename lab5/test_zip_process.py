from ZipProcessor import ZipProcessor
from ZipReplace import ZipReplace
import shutil
import zipfile
from pathlib import Path

test = ZipReplace('test.zip', 'Hello World!', 'Everything is ok!')
test.process_zip()
test.var.unzip_files()
for filename in test.var.temp_directory.iterdir():
	with filename.open() as file:
		contents = file.read()
		if contents == 'Everything is ok!':
			print('Everything works properly')
