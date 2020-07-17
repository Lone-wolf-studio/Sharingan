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
	# method to list out all models.py files path
	def get_all_dir_path(self):
		self.dir_path_list = [path for path, dir_name, file in os.walk(project_path)]
		return self.dir_path_list

if __name__ == "__main__":
	convert = ModelsConverter()
	dir_path_list = convert.get_all_dir_path()		
	