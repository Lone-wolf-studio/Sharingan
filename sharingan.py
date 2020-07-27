import argparse
import os
import subprocess
import time
import yaml

parser = argparse.ArgumentParser()
parser.add_argument('-project_path', '--project_path', help="Enter the path of project's root directory", required=True)
arguments = parser.parse_args()
project_path = arguments.project_path

class ModelsConverter(object):
	# method to get models.py files path
	def get_all_dir_path(self):
		self.dir_path_list = [path for path, dir_name, file in os.walk(project_path) for file_name in file if file_name=="models.py"]
		return self.dir_path_list

	
if __name__ == "__main__":
	convert = ModelsConverter()
	all_dirs_path = convert.get_all_dir_path()
	print(all_dirs_path)
	
	
